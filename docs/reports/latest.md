# Solana State Observatory — Snapshot

Generated **2026-08-22T13:44:11Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.48K tx/s |
| Slot time (sampled) | 0.3668 s |
| Epoch progress | 68.14% |
| Active validators | 685 |
| Delinquent stake | 0.0202% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 93.63 USD | 2.97% |
| DeFi TVL | 5.51B USD | — |
| Stablecoin supply | 15.81B USD | — |
| DEX volume | 3.60B USD | 30.15% |
| Protocol fees | 13.24M USD | 19.48% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 3.60BUSD | +29.47% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.07M SOL | 7% |
| `he1iusun…PauBtk` | 16.05M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.18M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.78M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.18M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.92M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.40M SOL | 0% |
| `9QU2QSxh…aM29mF` | 7.96M SOL | 7% |

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
