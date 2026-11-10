# Solana State Observatory — Snapshot

Generated **2026-11-10T18:16:15Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.05K tx/s |
| Slot time (sampled) | 0.2136 s |
| Epoch progress | 91.19% |
| Active validators | 657 |
| Delinquent stake | 0.2244% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 82.20 USD | -4.99% |
| DeFi TVL | 4.95B USD | — |
| Stablecoin supply | 14.58B USD | — |
| DEX volume | 1.49B USD | 42.59% |
| Protocol fees | 9.38M USD | 12.88% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 82.20USD | -11.83% |
| WARNING | TVL | 4.95BUSD | -8.47% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.90M SOL | 7% |
| `he1iusun…PauBtk` | 16.75M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 13.03M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.28M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.60M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.55M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.81M SOL | 7% |

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
