# Solana State Observatory — Snapshot

Generated **2026-09-19T09:29:53Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.99K tx/s |
| Slot time (sampled) | 0.2670 s |
| Epoch progress | 88.74% |
| Active validators | 677 |
| Delinquent stake | 0.0361% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 112.01 USD | 5.67% |
| DeFi TVL | 6.25B USD | — |
| Stablecoin supply | 15.48B USD | — |
| DEX volume | 3.26B USD | 25.68% |
| Protocol fees | 17.92M USD | 22.14% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 112.01USD | +10.43% |
| WARNING | DEX volume | 3.26BUSD | +25.68% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.82M SOL | 7% |
| `he1iusun…PauBtk` | 15.82M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.51M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.40M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.78M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.08M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.40M SOL | 7% |

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
