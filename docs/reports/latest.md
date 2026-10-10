# Solana State Observatory — Snapshot

Generated **2026-10-10T15:22:11Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 5.22K tx/s |
| Slot time (sampled) | 0.2196 s |
| Epoch progress | 94.26% |
| Active validators | 675 |
| Delinquent stake | 0.0022% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 110.37 USD | 0.77% |
| DeFi TVL | 6.21B USD | — |
| Stablecoin supply | 16.08B USD | — |
| DEX volume | 1.98B USD | -25.21% |
| Protocol fees | 13.91M USD | -7.66% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.79M SOL | 7% |
| `he1iusun…PauBtk` | 15.95M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.30M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.18M SOL | 0% |
| `CatzoSMU…gZDiqb` | 10.97M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.32M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.59M SOL | 7% |

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
