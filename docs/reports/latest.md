# Solana State Observatory — Snapshot

Generated **2026-11-18T19:36:37Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.29K tx/s |
| Slot time (sampled) | 0.2144 s |
| Epoch progress | 40.21% |
| Active validators | 659 |
| Delinquent stake | 0.3198% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 73.20 USD | 0.96% |
| DeFi TVL | 4.74B USD | — |
| Stablecoin supply | 13.14B USD | — |
| DEX volume | 1.51B USD | 2.01% |
| Protocol fees | 8.20M USD | -1.59% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 73.20USD | -11.72% |
| WARNING | Delinquent stake | 0.32% | +121.01% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 17.03M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.48M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.42M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.30M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.82M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.57M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.97M SOL | 7% |

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
