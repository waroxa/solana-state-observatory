# Solana State Observatory — Snapshot

Generated **2026-09-13T23:32:12Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.96K tx/s |
| Slot time (sampled) | 0.3180 s |
| Epoch progress | 32.63% |
| Active validators | 678 |
| Delinquent stake | 0.4357% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 99.55 USD | -2.16% |
| DeFi TVL | 5.89B USD | — |
| Stablecoin supply | 16.04B USD | — |
| DEX volume | 1.74B USD | -45.23% |
| Protocol fees | 13.52M USD | -24.39% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.44% | +548.85% |
| WARNING | DEX volume | 1.74BUSD | -39.18% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.57M SOL | 7% |
| `he1iusun…PauBtk` | 16.36M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.50M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.37M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.62M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.03M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.37M SOL | 7% |

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
