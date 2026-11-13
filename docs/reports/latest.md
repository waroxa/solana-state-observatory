# Solana State Observatory — Snapshot

Generated **2026-11-13T02:55:39Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.40K tx/s |
| Slot time (sampled) | 0.2154 s |
| Epoch progress | 10.85% |
| Active validators | 659 |
| Delinquent stake | 0.1318% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 79.94 USD | -4.02% |
| DeFi TVL | 5.03B USD | — |
| Stablecoin supply | 13.98B USD | — |
| DEX volume | 1.51B USD | -6.60% |
| Protocol fees | 8.49M USD | -16.53% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 79.94USD | -11.22% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.82M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.14M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.98M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.12M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.70M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.58M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.24M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.86M SOL | 7% |

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
