# Solana State Observatory — Snapshot

Generated **2026-09-03T19:52:00Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.37K tx/s |
| Slot time (sampled) | 0.3172 s |
| Epoch progress | 90.64% |
| Active validators | 676 |
| Delinquent stake | 0.0502% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 105.17 USD | 5.98% |
| DeFi TVL | 5.96B USD | — |
| Stablecoin supply | 15.98B USD | — |
| DEX volume | 2.29B USD | 5.42% |
| Protocol fees | 10.54M USD | -17.43% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.35M SOL | 7% |
| `he1iusun…PauBtk` | 16.33M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.46M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.30M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.57M SOL | 0% |
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
