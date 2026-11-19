# Solana State Observatory — Snapshot

Generated **2026-11-19T09:30:00Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.10K tx/s |
| Slot time (sampled) | 0.2140 s |
| Epoch progress | 94.00% |
| Active validators | 660 |
| Delinquent stake | 0.0155% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 74.33 USD | -0.60% |
| DeFi TVL | 4.79B USD | — |
| Stablecoin supply | 12.55B USD | — |
| DEX volume | 1.70B USD | 12.72% |
| Protocol fees | 9.97M USD | 22.51% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | TPS | 1.10Ktx/s | -35.69% |
| WARNING | SOL price | 74.33USD | -9.10% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `he1iusun…PauBtk` | 17.03M SOL | 0% |
| `CcaHc2L4…BzoTN1` | 16.48M SOL | 7% |
| `3N7s9zXM…eWiD5g` | 12.42M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.30M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.82M SOL | 10% |
| `CatzoSMU…gZDiqb` | 9.57M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.97M SOL | 7% |

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
