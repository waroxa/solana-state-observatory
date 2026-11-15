# Solana State Observatory — Snapshot

Generated **2026-11-15T09:55:35Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.17K tx/s |
| Slot time (sampled) | 0.2154 s |
| Epoch progress | 23.83% |
| Active validators | 661 |
| Delinquent stake | 0.1048% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 71.79 USD | -5.52% |
| DeFi TVL | 4.64B USD | — |
| Stablecoin supply | 13.92B USD | — |
| DEX volume | 1.61B USD | 3.42% |
| Protocol fees | 8.20M USD | -10.35% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | SOL price | 71.79USD | -18.86% |
| WARNING | TPS | 1.17Ktx/s | -30.45% |
| WARNING | TVL | 4.64BUSD | -10.99% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.93M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.40M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.61M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.14M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.75M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.64M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.20M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.94M SOL | 7% |

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
