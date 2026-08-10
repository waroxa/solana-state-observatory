# Solana State Observatory — Snapshot

Generated **2026-08-10T15:16:30Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.47K tx/s |
| Slot time (sampled) | 0.4213 s |
| Epoch progress | 87.36% |
| Active validators | 689 |
| Delinquent stake | 0.0927% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 76.09 USD | -1.00% |
| DeFi TVL | 4.84B USD | — |
| Stablecoin supply | 15.56B USD | — |
| DEX volume | 1.35B USD | -9.76% |
| Protocol fees | 9.10M USD | -1.21% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.09% | +1187.50% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.92M SOL | 7% |
| `he1iusun…PauBtk` | 15.98M SOL | 0% |
| `CatzoSMU…gZDiqb` | 12.49M SOL | 5% |
| `3N7s9zXM…eWiD5g` | 12.29M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.18M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.95M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.17M SOL | 0% |
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
