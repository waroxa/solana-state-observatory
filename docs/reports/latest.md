# Solana State Observatory — Snapshot

Generated **2026-09-09T13:43:21Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.90K tx/s |
| Slot time (sampled) | 0.3162 s |
| Epoch progress | 53.98% |
| Active validators | 678 |
| Delinquent stake | 0.3836% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 104.15 USD | 2.32% |
| DeFi TVL | 5.97B USD | — |
| Stablecoin supply | 16.21B USD | — |
| DEX volume | 2.71B USD | -0.36% |
| Protocol fees | 16.56M USD | 5.93% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.38% | +1087.62% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.44M SOL | 7% |
| `he1iusun…PauBtk` | 16.35M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.53M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.39M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.57M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.29M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.03M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.32M SOL | 7% |

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
