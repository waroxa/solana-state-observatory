# Solana State Observatory — Snapshot

Generated **2026-08-30T07:25:21Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.33K tx/s |
| Slot time (sampled) | 0.3176 s |
| Epoch progress | 5.04% |
| Active validators | 680 |
| Delinquent stake | 0.0099% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 105.17 USD | 1.34% |
| DeFi TVL | 5.90B USD | — |
| Stablecoin supply | 15.88B USD | — |
| DEX volume | 1.81B USD | -30.01% |
| Protocol fees | 11.17M USD | -28.99% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 105.17USD | +8.07% |
| WARNING | DEX volume | 1.81BUSD | -38.51% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.20M SOL | 7% |
| `he1iusun…PauBtk` | 16.09M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.39M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.48M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.45M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.29M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.02M SOL | 10% |
| `CvSb7wdQ…aKwycB` | 7.30M SOL | 5% |

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
