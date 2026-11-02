# Solana State Observatory — Snapshot

Generated **2026-11-02T17:03:28Z** · mainnet-beta · health score **93/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.10K tx/s |
| Slot time (sampled) | 0.2149 s |
| Epoch progress | 39.86% |
| Active validators | 665 |
| Delinquent stake | 1.0111% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 93.45 USD | -1.26% |
| DeFi TVL | 5.46B USD | — |
| Stablecoin supply | 14.94B USD | — |
| DEX volume | 905.60M USD | -5.03% |
| Protocol fees | 8.40M USD | 1.49% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 905.60MUSD | -47.76% |
| WARNING | Delinquent stake | 1.01% | +59.43% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.03M SOL | 7% |
| `he1iusun…PauBtk` | 16.71M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 13.04M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.43M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.58M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.45M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.80M SOL | 7% |

## Source coverage

12 of 12 source calls succeeded.

| Source | Metrics |
|---|---|
| [Solana JSON-RPC](https://api.mainnet-beta.solana.com) | network, validators, supply |
| [CoinGecko](https://www.coingecko.com/en/coins/solana) | SOL price |
| [DeFiLlama](https://defillama.com/chain/Solana) | TVL, stablecoins, DEX volume, fees |

## Methodology notes

- **TPS:** Recent RPC performance samples: total transactions divided by total sample seconds.
- **Slot time:** Recent RPC performance samples: total sample seconds divided by sampled slots.
- **Anomalies:** Current observation compared with the rolling median of up to 48 prior snapshots, plus explicit validator safety thresholds.
- **Health score:** Availability, slot performance, validator participation, and source coverage; diagnostic, not a protocol guarantee.

Machine-readable output: [`../data/latest.json`](../data/latest.json)
