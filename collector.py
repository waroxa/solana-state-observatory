#!/usr/bin/env python3
"""Collect a keyless snapshot of Solana ecosystem health.

The collector intentionally uses only Python's standard library. Every metric
keeps its source and freshness metadata, and a failed upstream never prevents
the remaining report from being generated.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import statistics
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
DATA_DIR = DOCS / "data"
REPORT_DIR = DOCS / "reports"
LATEST_PATH = DATA_DIR / "latest.json"
HISTORY_PATH = DATA_DIR / "history.json"
REPORT_PATH = REPORT_DIR / "latest.md"

RPC_URL = os.environ.get("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
USER_AGENT = "Solana-State-Observatory/1.0 (+https://github.com/)"
TIMEOUT = int(os.environ.get("OBSERVATORY_HTTP_TIMEOUT", "18"))
HISTORY_LIMIT = int(os.environ.get("OBSERVATORY_HISTORY_LIMIT", "336"))
SOURCE_CALLS = 12


class SourceError(RuntimeError):
    """A recoverable upstream source failure."""


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def request_json(
    url: str,
    *,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    timeout: int = TIMEOUT,
) -> Any:
    body = None
    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        raise SourceError(f"{url}: {exc}") from exc


def rpc(method: str, params: list[Any] | None = None) -> Any:
    data = request_json(
        RPC_URL,
        method="POST",
        payload={"jsonrpc": "2.0", "id": method, "method": method, "params": params or []},
    )
    if data.get("error"):
        raise SourceError(f"RPC {method}: {data['error']}")
    return data.get("result")


def safe(name: str, fn: Callable[[], Any], errors: list[dict[str, str]]) -> Any:
    try:
        return fn()
    except Exception as exc:  # Each source must fail independently.
        errors.append({"source": name, "message": str(exc)[:500]})
        return None


def find_chain(rows: list[dict[str, Any]], name: str = "Solana") -> dict[str, Any] | None:
    return next((row for row in rows if str(row.get("name", "")).lower() == name.lower()), None)


def coingecko() -> dict[str, Any]:
    return request_json(
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=solana&vs_currencies=usd&include_24hr_change=true&include_last_updated_at=true"
    )["solana"]


def defillama_chain() -> dict[str, Any]:
    row = find_chain(request_json("https://api.llama.fi/v2/chains"))
    if not row:
        raise SourceError("Solana was missing from DeFiLlama chains")
    return row


def defillama_stablecoins() -> dict[str, Any]:
    rows = request_json("https://stablecoins.llama.fi/stablecoinchains")
    row = find_chain(rows)
    if not row:
        raise SourceError("Solana was missing from DeFiLlama stablecoin chains")
    return row


def defillama_dex_volume() -> dict[str, Any]:
    return request_json(
        "https://api.llama.fi/overview/dexs/Solana"
        "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    )


def defillama_fees() -> dict[str, Any]:
    return request_json(
        "https://api.llama.fi/overview/fees/Solana"
        "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyFees"
    )


def compact_history(snapshot: dict[str, Any]) -> dict[str, Any]:
    metrics = snapshot.get("metrics", {})
    return {
        "generatedAt": snapshot["generatedAt"],
        "healthScore": snapshot.get("health", {}).get("score"),
        "tps": metrics.get("network", {}).get("tps"),
        "slotTimeSeconds": metrics.get("network", {}).get("slotTimeSeconds"),
        "solPriceUsd": metrics.get("economics", {}).get("solPriceUsd"),
        "tvlUsd": metrics.get("economics", {}).get("tvlUsd"),
        "dexVolume24hUsd": metrics.get("economics", {}).get("dexVolume24hUsd"),
        "delinquentStakePct": metrics.get("validators", {}).get("delinquentStakePct"),
    }


def load_history() -> list[dict[str, Any]]:
    try:
        data = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def finite(value: Any) -> float | None:
    try:
        number = float(value)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def pct_change(current: Any, previous: Any) -> float | None:
    a, b = finite(current), finite(previous)
    if a is None or b in (None, 0):
        return None
    return round((a - b) / abs(b) * 100, 2)


def median_baseline(history: list[dict[str, Any]], key: str, limit: int = 48) -> float | None:
    values = [finite(row.get(key)) for row in history[-limit:]]
    cleaned = [value for value in values if value is not None]
    return statistics.median(cleaned) if len(cleaned) >= 3 else None


def anomaly(
    metric: str,
    value: Any,
    baseline: Any,
    *,
    warning_pct: float,
    critical_pct: float,
    direction: str = "both",
    unit: str = "",
) -> dict[str, Any] | None:
    current, expected = finite(value), finite(baseline)
    if current is None or expected in (None, 0):
        return None
    delta = (current - expected) / abs(expected) * 100
    relevant = abs(delta) if direction == "both" else (-delta if direction == "down" else delta)
    if relevant < warning_pct:
        return None
    severity = "critical" if relevant >= critical_pct else "warning"
    return {
        "metric": metric,
        "severity": severity,
        "value": round(current, 4),
        "baseline": round(expected, 4),
        "deltaPct": round(delta, 2),
        "unit": unit,
        "method": "rolling median (up to 48 observations)",
    }


def health_score(metrics: dict[str, Any], errors: list[dict[str, str]]) -> dict[str, Any]:
    network = metrics["network"]
    validators = metrics["validators"]
    components: list[dict[str, Any]] = []

    rpc_ok = network.get("rpcHealth") == "ok"
    components.append({"name": "RPC availability", "score": 25 if rpc_ok else 0, "weight": 25})

    slot_time = finite(network.get("slotTimeSeconds"))
    slot_score = 25 if slot_time is not None and slot_time <= 0.55 else 15 if slot_time and slot_time <= 0.8 else 0
    components.append({"name": "Slot performance", "score": slot_score, "weight": 25})

    delinquent = finite(validators.get("delinquentStakePct"))
    validator_score = 25 if delinquent is not None and delinquent < 1 else 18 if delinquent is not None and delinquent < 3 else 5
    components.append({"name": "Validator participation", "score": validator_score, "weight": 25})

    source_penalty = min(25, round((len(errors) / SOURCE_CALLS) * 25))
    components.append({"name": "Source coverage", "score": 25 - source_penalty, "weight": 25})
    score = int(sum(item["score"] for item in components))
    status = "healthy" if score >= 85 else "watch" if score >= 65 else "degraded"
    return {"score": score, "status": status, "components": components}


def collect() -> dict[str, Any]:
    generated = utc_now()
    errors: list[dict[str, str]] = []

    epoch = safe("Solana RPC getEpochInfo", lambda: rpc("getEpochInfo"), errors) or {}
    slot = safe("Solana RPC getSlot", lambda: rpc("getSlot"), errors)
    block_height = safe("Solana RPC getBlockHeight", lambda: rpc("getBlockHeight"), errors)
    samples = safe("Solana RPC getRecentPerformanceSamples", lambda: rpc("getRecentPerformanceSamples", [12]), errors) or []
    votes = safe("Solana RPC getVoteAccounts", lambda: rpc("getVoteAccounts"), errors) or {}
    supply_result = safe("Solana RPC getSupply", lambda: rpc("getSupply", [{"commitment": "confirmed"}]), errors) or {}
    rpc_health = safe("Solana RPC getHealth", lambda: rpc("getHealth"), errors)
    price = safe("CoinGecko", coingecko, errors) or {}
    chain = safe("DeFiLlama chains", defillama_chain, errors) or {}
    stablecoins = safe("DeFiLlama stablecoins", defillama_stablecoins, errors) or {}
    dex = safe("DeFiLlama DEX volume", defillama_dex_volume, errors) or {}
    fees = safe("DeFiLlama fees", defillama_fees, errors) or {}

    sample_seconds = sum(finite(row.get("samplePeriodSecs")) or 0 for row in samples)
    transactions = sum(finite(row.get("numTransactions")) or 0 for row in samples)
    non_vote_transactions = sum(finite(row.get("numNonVoteTransactions")) or 0 for row in samples)
    sampled_slots = sum(finite(row.get("numSlots")) or 0 for row in samples)
    tps = round(transactions / sample_seconds, 2) if sample_seconds else None
    non_vote_tps = round(non_vote_transactions / sample_seconds, 2) if sample_seconds else None
    slot_time = round(sample_seconds / sampled_slots, 4) if sampled_slots else None

    current_validators = votes.get("current", []) or []
    delinquent_validators = votes.get("delinquent", []) or []
    current_stake = sum(int(row.get("activatedStake") or 0) for row in current_validators)
    delinquent_stake = sum(int(row.get("activatedStake") or 0) for row in delinquent_validators)
    all_stake = current_stake + delinquent_stake
    delinquent_pct = round(delinquent_stake / all_stake * 100, 4) if all_stake else None
    top_validators = sorted(current_validators, key=lambda row: int(row.get("activatedStake") or 0), reverse=True)[:8]

    supply = supply_result.get("value", supply_result) if isinstance(supply_result, dict) else {}
    lamports = 1_000_000_000
    epoch_progress = None
    if epoch.get("slotsInEpoch"):
        epoch_progress = round((epoch.get("slotIndex", 0) / epoch["slotsInEpoch"]) * 100, 2)

    tvl = finite(chain.get("tvl"))
    stablecoin_supply = finite(stablecoins.get("totalCirculatingUSD", {}).get("peggedUSD"))
    if stablecoin_supply is None:
        stablecoin_supply = finite(stablecoins.get("totalCirculatingUSD"))

    metrics = {
        "network": {
            "rpcHealth": rpc_health,
            "slot": slot,
            "blockHeight": block_height,
            "epoch": epoch.get("epoch"),
            "epochProgressPct": epoch_progress,
            "tps": tps,
            "nonVoteTps": non_vote_tps,
            "slotTimeSeconds": slot_time,
            "sampleWindowSeconds": round(sample_seconds, 2) if sample_seconds else None,
        },
        "validators": {
            "active": len(current_validators),
            "delinquent": len(delinquent_validators),
            "activeStakeSol": round(current_stake / lamports, 2),
            "delinquentStakeSol": round(delinquent_stake / lamports, 2),
            "delinquentStakePct": delinquent_pct,
            "topByStake": [
                {
                    "votePubkey": row.get("votePubkey"),
                    "nodePubkey": row.get("nodePubkey"),
                    "activatedStakeSol": round(int(row.get("activatedStake") or 0) / lamports, 2),
                    "commissionPct": row.get("commission"),
                    "lastVote": row.get("lastVote"),
                }
                for row in top_validators
            ],
        },
        "economics": {
            "solPriceUsd": finite(price.get("usd")),
            "solPriceChange24hPct": finite(price.get("usd_24h_change")),
            "solPriceUpdatedAt": iso(dt.datetime.fromtimestamp(price["last_updated_at"], dt.timezone.utc)) if price.get("last_updated_at") else None,
            "tvlUsd": tvl,
            "stablecoinSupplyUsd": stablecoin_supply,
            "dexVolume24hUsd": finite(dex.get("total24h")),
            "dexVolumeChange1dPct": finite(dex.get("change_1d")),
            "fees24hUsd": finite(fees.get("total24h")),
            "feesChange1dPct": finite(fees.get("change_1d")),
            "circulatingSupplySol": round((finite(supply.get("circulating")) or 0) / lamports, 2) if supply else None,
            "totalSupplySol": round((finite(supply.get("total")) or 0) / lamports, 2) if supply else None,
        },
    }

    history = load_history()
    anomalies: list[dict[str, Any]] = []
    candidates = [
        anomaly("TPS", tps, median_baseline(history, "tps"), warning_pct=25, critical_pct=45, direction="down", unit="tx/s"),
        anomaly("Slot time", slot_time, median_baseline(history, "slotTimeSeconds"), warning_pct=20, critical_pct=45, direction="up", unit="seconds"),
        anomaly("SOL price", price.get("usd"), median_baseline(history, "solPriceUsd"), warning_pct=8, critical_pct=15, unit="USD"),
        anomaly("TVL", tvl, median_baseline(history, "tvlUsd"), warning_pct=8, critical_pct=15, unit="USD"),
        anomaly("DEX volume", dex.get("total24h"), median_baseline(history, "dexVolume24hUsd"), warning_pct=25, critical_pct=50, unit="USD"),
        anomaly("Delinquent stake", delinquent_pct, median_baseline(history, "delinquentStakePct"), warning_pct=50, critical_pct=150, direction="up", unit="%"),
    ]
    anomalies.extend(item for item in candidates if item)
    if delinquent_pct is not None and delinquent_pct >= 3:
        anomalies.append({
            "metric": "Delinquent stake",
            "severity": "critical" if delinquent_pct >= 5 else "warning",
            "value": delinquent_pct,
            "baseline": 3,
            "deltaPct": round((delinquent_pct - 3) / 3 * 100, 2),
            "unit": "%",
            "method": "absolute safety threshold",
        })

    snapshot: dict[str, Any] = {
        "schemaVersion": "1.0.0",
        "generatedAt": iso(generated),
        "network": "mainnet-beta",
        "health": {},
        "metrics": metrics,
        "anomalies": sorted(anomalies, key=lambda item: item["severity"] != "critical"),
        "coverage": {
            "successfulSources": SOURCE_CALLS - len(errors),
            "totalSources": SOURCE_CALLS,
            "partial": bool(errors),
            "errors": errors,
        },
        "sources": [
            {"name": "Solana JSON-RPC", "url": RPC_URL, "metrics": ["network", "validators", "supply"]},
            {"name": "CoinGecko", "url": "https://www.coingecko.com/en/coins/solana", "metrics": ["SOL price"]},
            {"name": "DeFiLlama", "url": "https://defillama.com/chain/Solana", "metrics": ["TVL", "stablecoins", "DEX volume", "fees"]},
        ],
        "methodology": {
            "tps": "Recent RPC performance samples: total transactions divided by total sample seconds.",
            "slotTime": "Recent RPC performance samples: total sample seconds divided by sampled slots.",
            "anomalies": "Current observation compared with the rolling median of up to 48 prior snapshots, plus explicit validator safety thresholds.",
            "healthScore": "Availability, slot performance, validator participation, and source coverage; diagnostic, not a protocol guarantee.",
        },
    }
    snapshot["health"] = health_score(metrics, errors)
    return snapshot


def fmt(value: Any, suffix: str = "", decimals: int = 2) -> str:
    number = finite(value)
    if number is None:
        return "Unavailable"
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.{decimals}f}B{suffix}"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.{decimals}f}M{suffix}"
    if abs(number) >= 1_000:
        return f"{number / 1_000:.{decimals}f}K{suffix}"
    return f"{number:.{decimals}f}{suffix}"


def render_markdown(snapshot: dict[str, Any]) -> str:
    m = snapshot["metrics"]
    anomaly_rows = "\n".join(
        f"| {item['severity'].upper()} | {item['metric']} | {fmt(item['value'], item.get('unit', ''))} | {item['deltaPct']:+.2f}% |"
        for item in snapshot["anomalies"]
    ) or "| — | No anomaly detected | — | — |"
    source_rows = "\n".join(
        f"| [{source['name']}]({source['url']}) | {', '.join(source['metrics'])} |"
        for source in snapshot["sources"]
    )
    top_rows = "\n".join(
        f"| `{row['votePubkey'][:8]}…{row['votePubkey'][-6:]}` | {fmt(row['activatedStakeSol'], ' SOL')} | {row['commissionPct']}% |"
        for row in m["validators"].get("topByStake", [])
    ) or "| — | — | — |"

    return f"""# Solana State Observatory — Snapshot

Generated **{snapshot['generatedAt']}** · mainnet-beta · health score **{snapshot['health']['score']}/100 ({snapshot['health']['status']})**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | {m['network'].get('rpcHealth') or 'Unavailable'} |
| Throughput (sampled) | {fmt(m['network'].get('tps'), ' tx/s')} |
| Slot time (sampled) | {fmt(m['network'].get('slotTimeSeconds'), ' s', 4)} |
| Epoch progress | {fmt(m['network'].get('epochProgressPct'), '%')} |
| Active validators | {fmt(m['validators'].get('active'), '', 0)} |
| Delinquent stake | {fmt(m['validators'].get('delinquentStakePct'), '%', 4)} |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | {fmt(m['economics'].get('solPriceUsd'), ' USD')} | {fmt(m['economics'].get('solPriceChange24hPct'), '%')} |
| DeFi TVL | {fmt(m['economics'].get('tvlUsd'), ' USD')} | — |
| Stablecoin supply | {fmt(m['economics'].get('stablecoinSupplyUsd'), ' USD')} | — |
| DEX volume | {fmt(m['economics'].get('dexVolume24hUsd'), ' USD')} | {fmt(m['economics'].get('dexVolumeChange1dPct'), '%')} |
| Protocol fees | {fmt(m['economics'].get('fees24hUsd'), ' USD')} | {fmt(m['economics'].get('feesChange1dPct'), '%')} |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
{anomaly_rows}

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
{top_rows}

## Source coverage

{snapshot['coverage']['successfulSources']} of {snapshot['coverage']['totalSources']} source calls succeeded.

| Source | Metrics |
|---|---|
{source_rows}

## Methodology notes

- **TPS:** {snapshot['methodology']['tps']}
- **Slot time:** {snapshot['methodology']['slotTime']}
- **Anomalies:** {snapshot['methodology']['anomalies']}
- **Health score:** {snapshot['methodology']['healthScore']}

Machine-readable output: [`../data/latest.json`](../data/latest.json)
"""


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temp_name = handle.name
    os.replace(temp_name, path)


def write_outputs(snapshot: dict[str, Any]) -> None:
    history = load_history()
    history.append(compact_history(snapshot))
    history = history[-HISTORY_LIMIT:]
    atomic_write(LATEST_PATH, json.dumps(snapshot, indent=2, sort_keys=False) + "\n")
    atomic_write(HISTORY_PATH, json.dumps(history, indent=2, sort_keys=False) + "\n")
    atomic_write(REPORT_PATH, render_markdown(snapshot))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdout", action="store_true", help="print the generated JSON")
    parser.add_argument("--no-write", action="store_true", help="do not update generated files")
    args = parser.parse_args()
    started = time.monotonic()
    snapshot = collect()
    snapshot["collectorDurationSeconds"] = round(time.monotonic() - started, 3)
    if not args.no_write:
        write_outputs(snapshot)
    if args.stdout:
        print(json.dumps(snapshot, indent=2))
    print(
        f"snapshot {snapshot['generatedAt']} | health {snapshot['health']['score']}/100 | "
        f"sources {snapshot['coverage']['successfulSources']}/{snapshot['coverage']['totalSources']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
