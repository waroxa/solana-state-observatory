# Solana State Observatory — Snapshot

Generated **2026-11-01T20:49:48Z** · mainnet-beta · health score **93/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.58K tx/s |
| Slot time (sampled) | 0.2133 s |
| Epoch progress | 61.22% |
| Active validators | 662 |
| Delinquent stake | 1.0499% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 94.18 USD | -1.50% |
| DeFi TVL | 5.40B USD | — |
| Stablecoin supply | 15.05B USD | — |
| DEX volume | 953.59M USD | -54.96% |
| Protocol fees | 8.27M USD | -26.39% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 1.05% | +261.91% |
| WARNING | DEX volume | 953.59MUSD | -49.46% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.03M SOL | 7% |
| `he1iusun…PauBtk` | 16.70M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.94M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.43M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.58M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.45M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.79M SOL | 7% |

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
