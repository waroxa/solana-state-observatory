# Solana State Observatory — Snapshot

Generated **2026-11-17T20:53:41Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.94K tx/s |
| Slot time (sampled) | 0.2157 s |
| Epoch progress | 52.47% |
| Active validators | 661 |
| Delinquent stake | 0.0129% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 72.80 USD | 1.85% |
| DeFi TVL | 4.72B USD | — |
| Stablecoin supply | 13.61B USD | — |
| DEX volume | 1.48B USD | 9.42% |
| Protocol fees | 8.33M USD | 16.23% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 72.80USD | -12.92% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 16.83M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.44M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.43M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.14M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.80M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.63M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
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
