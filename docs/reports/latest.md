# Solana State Observatory — Snapshot

Generated **2026-09-29T17:01:23Z** · mainnet-beta · health score **98/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 5.11K tx/s |
| Slot time (sampled) | 0.2675 s |
| Epoch progress | 60.85% |
| Active validators | 672 |
| Delinquent stake | 0.0537% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | Unavailable | Unavailable |
| DeFi TVL | 6.58B USD | — |
| Stablecoin supply | 16.01B USD | — |
| DEX volume | 2.66B USD | 38.18% |
| Protocol fees | 17.51M USD | 13.56% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.82M SOL | 7% |
| `he1iusun…PauBtk` | 15.89M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.34M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.30M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.21M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.24M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.22M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.64M SOL | 7% |

## Source coverage

11 of 12 source calls succeeded.

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
