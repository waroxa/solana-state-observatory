# Solana State Observatory — Snapshot

Generated **2026-08-31T20:49:46Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.09K tx/s |
| Slot time (sampled) | 0.3172 s |
| Epoch progress | 3.28% |
| Active validators | 679 |
| Delinquent stake | 0.1917% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 103.77 USD | -1.10% |
| DeFi TVL | 5.85B USD | — |
| Stablecoin supply | 15.65B USD | — |
| DEX volume | 1.93B USD | 15.50% |
| Protocol fees | 12.31M USD | 9.75% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.19% | +405.80% |
| WARNING | DEX volume | 1.93BUSD | -34.25% |

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
