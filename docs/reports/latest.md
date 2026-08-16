# Solana State Observatory — Snapshot

Generated **2026-08-16T01:56:37Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.50K tx/s |
| Slot time (sampled) | 0.4133 s |
| Epoch progress | 47.75% |
| Active validators | 688 |
| Delinquent stake | 0.0166% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 75.35 USD | 0.02% |
| DeFi TVL | 4.81B USD | — |
| Stablecoin supply | 15.35B USD | — |
| DEX volume | 1.23B USD | -23.08% |
| Protocol fees | 8.10M USD | 0.62% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

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
