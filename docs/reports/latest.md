# Solana State Observatory — Snapshot

Generated **2026-08-17T03:12:25Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.31K tx/s |
| Slot time (sampled) | 0.4147 s |
| Epoch progress | 98.41% |
| Active validators | 687 |
| Delinquent stake | 0.0325% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 75.46 USD | -0.12% |
| DeFi TVL | 4.79B USD | — |
| Stablecoin supply | 15.36B USD | — |
| DEX volume | 1.05B USD | -9.86% |
| Protocol fees | 6.62M USD | -18.76% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | Delinquent stake | 0.03% | +95.78% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.16M SOL | 7% |
| `he1iusun…PauBtk` | 15.97M SOL | 0% |
| `CatzoSMU…gZDiqb` | 12.49M SOL | 5% |
| `3N7s9zXM…eWiD5g` | 12.27M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.18M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.98M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.30M SOL | 0% |
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
