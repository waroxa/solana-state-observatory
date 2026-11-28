# Solana State Observatory — Snapshot

Generated **2026-11-28T13:03:04Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 960.89 tx/s |
| Slot time (sampled) | 0.2123 s |
| Epoch progress | 45.11% |
| Active validators | 655 |
| Delinquent stake | 0.0268% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 70.85 USD | -3.04% |
| DeFi TVL | 4.60B USD | — |
| Stablecoin supply | 12.93B USD | — |
| DEX volume | 1.03B USD | 18.48% |
| Protocol fees | 5.58M USD | -9.28% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | TPS | 960.89tx/s | -42.39% |
| WARNING | DEX volume | 1.03BUSD | -32.22% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.82M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 15.94M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.43M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.24M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.92M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.63M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.30M SOL | 7% |
| `9QU2QSxh…aM29mF` | 8.05M SOL | 7% |

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
