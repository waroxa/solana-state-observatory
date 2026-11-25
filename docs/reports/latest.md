# Solana State Observatory — Snapshot

Generated **2026-11-25T10:29:31Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.26K tx/s |
| Slot time (sampled) | 0.2168 s |
| Epoch progress | 55.84% |
| Active validators | 660 |
| Delinquent stake | 0.0195% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 67.69 USD | -4.19% |
| DeFi TVL | 4.49B USD | — |
| Stablecoin supply | 12.99B USD | — |
| DEX volume | 1.65B USD | -8.90% |
| Protocol fees | 7.38M USD | -12.64% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | TPS | 1.26Ktx/s | -26.66% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 17.00M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 15.96M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.42M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.24M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.89M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.62M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.28M SOL | 7% |
| `9QU2QSxh…aM29mF` | 8.02M SOL | 7% |

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
