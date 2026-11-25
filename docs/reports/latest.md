# Solana State Observatory — Snapshot

Generated **2026-11-25T20:11:46Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.25K tx/s |
| Slot time (sampled) | 0.2151 s |
| Epoch progress | 93.44% |
| Active validators | 657 |
| Delinquent stake | 0.0730% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 70.34 USD | 1.90% |
| DeFi TVL | 4.54B USD | — |
| Stablecoin supply | 12.87B USD | — |
| DEX volume | 1.46B USD | -19.33% |
| Protocol fees | 7.15M USD | -15.53% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | Delinquent stake | 0.07% | +105.63% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 17.00M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 15.96M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.42M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.24M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.89M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.62M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.28M SOL | 7% |
| `9QU2QSxh…aM29mF` | 8.02M SOL | 7% |

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
