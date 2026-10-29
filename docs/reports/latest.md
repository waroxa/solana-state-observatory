# Solana State Observatory — Snapshot

Generated **2026-10-29T19:41:19Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.89K tx/s |
| Slot time (sampled) | 0.2154 s |
| Epoch progress | 76.48% |
| Active validators | 663 |
| Delinquent stake | 0.8037% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 100.06 USD | -2.10% |
| DeFi TVL | 5.69B USD | — |
| Stablecoin supply | 15.25B USD | — |
| DEX volume | 1.73B USD | 9.50% |
| Protocol fees | 10.35M USD | -7.89% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.80% | +960.99% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.03M SOL | 7% |
| `he1iusun…PauBtk` | 16.67M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.88M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.76M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.71M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.47M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.76M SOL | 7% |

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
