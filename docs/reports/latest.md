# Solana State Observatory — Snapshot

Generated **2026-08-20T01:51:20Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.87K tx/s |
| Slot time (sampled) | 0.4140 s |
| Epoch progress | 40.03% |
| Active validators | 688 |
| Delinquent stake | 0.0230% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 85.24 USD | 11.13% |
| DeFi TVL | 5.20B USD | — |
| Stablecoin supply | 15.68B USD | — |
| DEX volume | 2.59B USD | 41.07% |
| Protocol fees | 10.25M USD | 16.84% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 85.24USD | +10.27% |
| WARNING | DEX volume | 2.59BUSD | +42.42% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.10M SOL | 7% |
| `he1iusun…PauBtk` | 16.01M SOL | 0% |
| `CatzoSMU…gZDiqb` | 12.41M SOL | 5% |
| `3N7s9zXM…eWiD5g` | 12.20M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.19M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.99M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.31M SOL | 0% |
| `9QU2QSxh…aM29mF` | 7.99M SOL | 7% |

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
