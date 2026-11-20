# Solana State Observatory — Snapshot

Generated **2026-11-20T17:17:11Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.33K tx/s |
| Slot time (sampled) | 0.2142 s |
| Epoch progress | 17.11% |
| Active validators | 662 |
| Delinquent stake | 0.0171% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 68.88 USD | -5.43% |
| DeFi TVL | 4.62B USD | — |
| Stablecoin supply | 12.87B USD | — |
| DEX volume | 1.90B USD | 4.89% |
| Protocol fees | 9.31M USD | -14.66% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 68.88USD | -13.88% |
| WARNING | DEX volume | 1.90BUSD | +26.86% |

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
