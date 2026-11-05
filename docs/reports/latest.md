# Solana State Observatory — Snapshot

Generated **2026-11-05T17:39:32Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 2.64K tx/s |
| Slot time (sampled) | 0.2142 s |
| Epoch progress | 22.42% |
| Active validators | 662 |
| Delinquent stake | 0.1861% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 89.58 USD | -6.26% |
| DeFi TVL | 5.42B USD | — |
| Stablecoin supply | 14.90B USD | — |
| DEX volume | 2.39B USD | 26.82% |
| Protocol fees | 11.23M USD | -1.62% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 2.39BUSD | +37.62% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.06M SOL | 7% |
| `he1iusun…PauBtk` | 16.74M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 13.02M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.43M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.53M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.46M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.86M SOL | 7% |

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
