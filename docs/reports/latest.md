# Solana State Observatory — Snapshot

Generated **2026-11-14T13:48:02Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.37K tx/s |
| Slot time (sampled) | 0.2141 s |
| Epoch progress | 45.85% |
| Active validators | 662 |
| Delinquent stake | 0.0920% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 75.64 USD | -7.69% |
| DeFi TVL | 4.84B USD | — |
| Stablecoin supply | 13.99B USD | — |
| DEX volume | 1.56B USD | 3.80% |
| Protocol fees | 9.14M USD | 14.46% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | SOL price | 75.64USD | -15.54% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.96M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.37M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.61M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.14M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.74M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.57M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.20M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.91M SOL | 7% |

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
