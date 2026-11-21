# Solana State Observatory — Snapshot

Generated **2026-11-21T04:17:07Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.69K tx/s |
| Slot time (sampled) | 0.2151 s |
| Epoch progress | 59.69% |
| Active validators | 662 |
| Delinquent stake | 0.0171% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 65.64 USD | -9.53% |
| DeFi TVL | 4.57B USD | — |
| Stablecoin supply | 12.95B USD | — |
| DEX volume | 1.84B USD | -3.57% |
| Protocol fees | 8.96M USD | -3.51% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 65.64USD | -14.63% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 17.04M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.35M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.42M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.31M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.78M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.56M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.99M SOL | 7% |

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
