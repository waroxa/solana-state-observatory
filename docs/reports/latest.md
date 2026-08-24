# Solana State Observatory — Snapshot

Generated **2026-08-24T18:15:10Z** · mainnet-beta · health score **93/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.43K tx/s |
| Slot time (sampled) | 0.3672 s |
| Epoch progress | 87.75% |
| Active validators | 683 |
| Delinquent stake | 1.3201% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 95.90 USD | 0.71% |
| DeFi TVL | 5.62B USD | — |
| Stablecoin supply | 15.73B USD | — |
| DEX volume | 2.94B USD | -21.27% |
| Protocol fees | 12.65M USD | 5.30% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 1.32% | +1004.22% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.98M SOL | 7% |
| `he1iusun…PauBtk` | 16.03M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.21M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.73M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.17M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.88M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.48M SOL | 0% |
| `9QU2QSxh…aM29mF` | 7.93M SOL | 7% |

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
