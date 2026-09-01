# Solana State Observatory — Snapshot

Generated **2026-09-01T00:37:02Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.95K tx/s |
| Slot time (sampled) | 0.3175 s |
| Epoch progress | 13.21% |
| Active validators | 679 |
| Delinquent stake | 0.0307% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 103.35 USD | 0.89% |
| DeFi TVL | 5.99B USD | — |
| Stablecoin supply | 15.73B USD | — |
| DEX volume | 2.10B USD | 8.90% |
| Protocol fees | 12.54M USD | 1.88% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 2.10BUSD | -28.40% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.17M SOL | 7% |
| `he1iusun…PauBtk` | 16.28M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.43M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.48M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.46M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.29M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.04M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.22M SOL | 7% |

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
