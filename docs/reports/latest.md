# Solana State Observatory — Snapshot

Generated **2026-08-14T19:55:57Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.02K tx/s |
| Slot time (sampled) | 0.4213 s |
| Epoch progress | 87.61% |
| Active validators | 689 |
| Delinquent stake | 0.0138% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 74.99 USD | -1.43% |
| DeFi TVL | 4.80B USD | — |
| Stablecoin supply | 15.35B USD | — |
| DEX volume | 1.94B USD | 12.58% |
| Protocol fees | 10.15M USD | 4.91% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.06M SOL | 7% |
| `he1iusun…PauBtk` | 15.97M SOL | 0% |
| `CatzoSMU…gZDiqb` | 12.48M SOL | 5% |
| `3N7s9zXM…eWiD5g` | 12.36M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.16M SOL | 7% |
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
