# Solana State Observatory — Snapshot

Generated **2026-11-23T09:51:05Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.04K tx/s |
| Slot time (sampled) | 0.2151 s |
| Epoch progress | 67.30% |
| Active validators | 662 |
| Delinquent stake | 0.0119% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 72.15 USD | 2.96% |
| DeFi TVL | 4.69B USD | — |
| Stablecoin supply | 13.07B USD | — |
| DEX volume | 1.19B USD | -11.85% |
| Protocol fees | 6.01M USD | -20.50% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | TPS | 1.04Ktx/s | -39.55% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.92M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.35M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.40M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.24M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.84M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.61M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.27M SOL | 7% |
| `9QU2QSxh…aM29mF` | 8.00M SOL | 7% |

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
