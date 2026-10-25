# Solana State Observatory — Snapshot

Generated **2026-10-25T14:21:47Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.14K tx/s |
| Slot time (sampled) | 0.2118 s |
| Epoch progress | 79.95% |
| Active validators | 665 |
| Delinquent stake | 0.0491% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 100.66 USD | 0.04% |
| DeFi TVL | 5.75B USD | — |
| Stablecoin supply | 15.50B USD | — |
| DEX volume | 1.42B USD | -28.74% |
| Protocol fees | 10.05M USD | -4.82% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.05% | +319.66% |
| WARNING | TPS | 2.14Ktx/s | -40.13% |
| WARNING | DEX volume | 1.42BUSD | -28.74% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.10M SOL | 7% |
| `he1iusun…PauBtk` | 16.65M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.59M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.88M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.72M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.48M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.79M SOL | 7% |

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
