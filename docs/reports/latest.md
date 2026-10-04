# Solana State Observatory — Snapshot

Generated **2026-10-04T23:08:46Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.86K tx/s |
| Slot time (sampled) | 0.2697 s |
| Epoch progress | 53.63% |
| Active validators | 671 |
| Delinquent stake | 0.0272% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 121.62 USD | 1.67% |
| DeFi TVL | 6.73B USD | — |
| Stablecoin supply | 16.51B USD | — |
| DEX volume | 1.55B USD | -43.70% |
| Protocol fees | 12.93M USD | -25.70% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 1.55BUSD | -38.79% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.94M SOL | 7% |
| `he1iusun…PauBtk` | 15.93M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.35M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.31M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.14M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.24M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.62M SOL | 7% |

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
