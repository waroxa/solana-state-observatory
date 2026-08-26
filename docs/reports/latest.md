# Solana State Observatory — Snapshot

Generated **2026-08-26T22:30:23Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.79K tx/s |
| Slot time (sampled) | 0.3683 s |
| Epoch progress | 6.82% |
| Active validators | 685 |
| Delinquent stake | 0.0526% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 100.20 USD | 2.99% |
| DeFi TVL | 5.60B USD | — |
| Stablecoin supply | 15.86B USD | — |
| DEX volume | 2.93B USD | -2.04% |
| Protocol fees | 13.24M USD | -8.67% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.06M SOL | 7% |
| `he1iusun…PauBtk` | 16.03M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.31M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.75M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `8GbwASqd…GJF8iD` | 9.05M SOL | 0% |
| `51JBzSTU…zgUNAm` | 8.90M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.85M SOL | 7% |

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
