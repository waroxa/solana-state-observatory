# Solana State Observatory — Snapshot

Generated **2026-10-30T09:59:14Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.37K tx/s |
| Slot time (sampled) | 0.2132 s |
| Epoch progress | 32.23% |
| Active validators | 665 |
| Delinquent stake | 0.6952% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 96.70 USD | -3.50% |
| DeFi TVL | 5.44B USD | — |
| Stablecoin supply | 15.11B USD | — |
| DEX volume | 1.92B USD | 11.02% |
| Protocol fees | 12.27M USD | 16.36% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.70% | +566.54% |
| WARNING | TPS | 1.37Ktx/s | -27.62% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.97M SOL | 7% |
| `he1iusun…PauBtk` | 16.68M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.92M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.50M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.66M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.47M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.78M SOL | 7% |

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
