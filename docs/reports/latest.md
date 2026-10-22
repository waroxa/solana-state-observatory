# Solana State Observatory — Snapshot

Generated **2026-10-22T13:11:58Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.84K tx/s |
| Slot time (sampled) | 0.2128 s |
| Epoch progress | 92.51% |
| Active validators | 668 |
| Delinquent stake | 0.0050% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 104.16 USD | -2.83% |
| DeFi TVL | 5.91B USD | — |
| Stablecoin supply | 15.83B USD | — |
| DEX volume | 2.27B USD | -6.87% |
| Protocol fees | 11.89M USD | -9.76% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | TPS | 2.84Ktx/s | -41.93% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.13M SOL | 7% |
| `he1iusun…PauBtk` | 15.96M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.55M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.93M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.73M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.48M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
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
