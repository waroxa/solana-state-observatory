# Solana State Observatory — Snapshot

Generated **2026-10-27T20:05:05Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.29K tx/s |
| Slot time (sampled) | 0.2138 s |
| Epoch progress | 90.58% |
| Active validators | 665 |
| Delinquent stake | 0.0852% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 100.98 USD | 0.77% |
| DeFi TVL | 5.72B USD | — |
| Stablecoin supply | 15.35B USD | — |
| DEX volume | 2.07B USD | 42.91% |
| Protocol fees | 11.67M USD | 25.60% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | Delinquent stake | 0.09% | +73.52% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.06M SOL | 7% |
| `he1iusun…PauBtk` | 16.64M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.66M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.81M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.72M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.49M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.21M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.75M SOL | 7% |

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
