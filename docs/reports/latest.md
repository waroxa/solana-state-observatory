# Solana State Observatory — Snapshot

Generated **2026-09-19T21:45:40Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.84K tx/s |
| Slot time (sampled) | 0.2687 s |
| Epoch progress | 27.05% |
| Active validators | 677 |
| Delinquent stake | 0.0359% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 110.30 USD | -2.56% |
| DeFi TVL | 6.23B USD | — |
| Stablecoin supply | 16.50B USD | — |
| DEX volume | 3.54B USD | 36.44% |
| Protocol fees | 17.46M USD | 18.99% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 110.30USD | +8.74% |
| WARNING | DEX volume | 3.54BUSD | +36.44% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.85M SOL | 7% |
| `he1iusun…PauBtk` | 15.82M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.50M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.36M SOL | 5% |
| `8GbwASqd…GJF8iD` | 9.79M SOL | 0% |
| `26pV97Ce…c53dJx` | 9.25M SOL | 7% |
| `51JBzSTU…zgUNAm` | 9.12M SOL | 10% |
| `9QU2QSxh…aM29mF` | 7.43M SOL | 7% |

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
