# Solana State Observatory — Snapshot

Generated **2026-10-06T00:20:26Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.45K tx/s |
| Slot time (sampled) | 0.2670 s |
| Epoch progress | 32.01% |
| Active validators | 672 |
| Delinquent stake | 0.0185% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 120.94 USD | -0.38% |
| DeFi TVL | 6.80B USD | — |
| Stablecoin supply | 16.75B USD | — |
| DEX volume | 1.71B USD | 9.92% |
| Protocol fees | 16.12M USD | 24.70% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 1.71BUSD | -32.60% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.92M SOL | 7% |
| `he1iusun…PauBtk` | 15.94M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.29M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.31M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.14M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.26M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.25M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.63M SOL | 7% |

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
