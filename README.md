# Solana State Observatory

An autonomous, keyless report on Solana network health, validator participation, and economic activity. It produces three synchronized outputs from one collection run:

- a responsive interactive dashboard (`docs/index.html`)
- a human-readable report (`docs/reports/latest.md`)
- machine-readable observations (`docs/data/latest.json` and `history.json`)

The implementation is intentionally dependency-free: Python standard library for collection and plain HTML/CSS/JavaScript for presentation.

## Why this exists

Solana telemetry is useful but fragmented across RPC methods, market data providers, and ecosystem dashboards. This project turns those inputs into a single observation with explicit freshness, source coverage, and failure states. It does not silently substitute stale values when an upstream source fails.

## Current coverage

| Dimension | Metrics | Source |
|---|---|---|
| Network | RPC health, slot, block height, epoch progress, sampled TPS, non-vote TPS, slot time | Solana JSON-RPC |
| Validators | active/delinquent counts, activated stake, delinquent stake ratio, top validators, commission | Solana JSON-RPC |
| Supply | circulating and total SOL supply | Solana JSON-RPC |
| Markets | SOL/USD and 24-hour change | CoinGecko |
| DeFi | TVL, stablecoin supply, DEX volume, protocol fees | DeFiLlama |
| Intelligence | health score, rolling-baseline anomaly detection, source coverage | locally derived |

## Run it

Requirements: Python 3.11+ and internet access for the live collection.

```bash
python3 collector.py
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`.

Run the offline test suite:

```bash
python3 -m unittest discover -s tests -v
```

Print a snapshot without changing generated files:

```bash
python3 collector.py --stdout --no-write
```

## Architecture

```text
Solana JSON-RPC ─┐
CoinGecko ───────┼─> collector.py ─┬─> docs/data/latest.json
DeFiLlama ───────┘                 ├─> docs/data/history.json
                                   └─> docs/reports/latest.md
                                                │
                                                └─> docs/ dashboard
```

Each upstream call is isolated with a recoverable failure boundary. A rate limit or outage reduces the coverage score and is surfaced in `coverage.errors`; it does not erase metrics from sources that still work.

## Automation strategy

`.github/workflows/update-data.yml` runs twice per hour:

1. check out the repository;
2. run the offline unit tests;
3. collect a fresh public observation;
4. commit only changed generated data and reports.

`.github/workflows/pages.yml` deploys the `docs/` directory after a relevant push. No secrets or API keys are required. A custom RPC can be used locally through `SOLANA_RPC_URL` without committing it.

The bounded history keeps the latest 336 observations (roughly one week at a 30-minute cadence), which controls repository growth while supporting temporal comparisons.

## Anomaly detection

The engine compares the current value with the rolling median of up to 48 prior observations. A median is used instead of a mean to reduce sensitivity to isolated spikes.

| Signal | Warning | Critical | Direction |
|---|---:|---:|---|
| TPS | 25% | 45% | drop |
| Slot time | 20% | 45% | increase |
| SOL price | 8% | 15% | either |
| TVL | 8% | 15% | either |
| DEX volume | 25% | 50% | either |
| Delinquent stake | 50% | 150% | increase |

Delinquent stake also has an explicit safety threshold at 3%. Every anomaly includes the observation, baseline, percentage delta, severity, unit, and method. Detection activates after at least three historical observations exist.

## Health score

The 100-point diagnostic score has four equally weighted components:

- RPC availability
- slot performance
- validator participation
- source coverage

This is an operational summary, not a protocol guarantee, investment signal, or financial recommendation. The component breakdown is included in JSON and rendered in the dashboard.

## Data semantics and caveats

- Sampled TPS includes vote transactions; `nonVoteTps` is also exported separately.
- Slot time and TPS are calculated from the same recent RPC performance window.
- DeFiLlama and CoinGecko timestamps and aggregation rules can differ from on-chain boundaries.
- Public RPC endpoints can rate-limit automation. A custom endpoint can be supplied with `SOLANA_RPC_URL` at runtime.
- The dashboard labels missing data as unavailable. It does not invent or backfill a value.
- This project is informational and is not financial advice.

## Repository map

```text
collector.py                       keyless collector, analysis, report renderer
tests/test_collector.py            offline tests for core transformations
docs/index.html                    semantic dashboard shell
docs/styles.css                    responsive token-based dark theme
docs/app.js                        data binding and accessible SVG charts
docs/data/latest.json              full current snapshot
docs/data/history.json             bounded temporal series
docs/reports/latest.md             generated human report
.github/workflows/update-data.yml  scheduled collection
.github/workflows/pages.yml        static deployment
```

## License

MIT. See [LICENSE](LICENSE).
