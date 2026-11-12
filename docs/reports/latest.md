# Solana State Observatory — Snapshot

Generated **2026-11-12T08:18:30Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.21K tx/s |
| Slot time (sampled) | 0.2157 s |
| Epoch progress | 38.77% |
| Active validators | 661 |
| Delinquent stake | 0.1580% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 82.83 USD | -0.49% |
| DeFi TVL | 5.04B USD | — |
| Stablecoin supply | 13.82B USD | — |
| DEX volume | 1.64B USD | 22.25% |
| Protocol fees | 9.32M USD | 10.97% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 82.83USD | -8.15% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.79M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.12M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 13.03M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.12M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.68M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.58M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.84M SOL | 7% |

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
