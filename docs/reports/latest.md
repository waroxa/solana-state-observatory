# Solana State Observatory — Snapshot

Generated **2026-08-04T15:09:40Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.22K tx/s |
| Slot time (sampled) | 0.4235 s |
| Epoch progress | 3.16% |
| Active validators | 692 |
| Delinquent stake | 0.0004% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 73.83 USD | 0.38% |
| DeFi TVL | 4.77B USD | — |
| Stablecoin supply | 15.77B USD | — |
| DEX volume | 1.70B USD | 26.84% |
| Protocol fees | 8.41M USD | 11.90% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 1.70BUSD | +26.84% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.81M SOL | 7% |
| `he1iusun…PauBtk` | 16.00M SOL | 0% |
| `CatzoSMU…gZDiqb` | 12.47M SOL | 5% |
| `3N7s9zXM…eWiD5g` | 12.27M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.19M SOL | 7% |
| `51JBzSTU…zgUNAm` | 8.84M SOL | 10% |
| `8GbwASqd…GJF8iD` | 8.16M SOL | 0% |
| `9QU2QSxh…aM29mF` | 7.90M SOL | 7% |

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
