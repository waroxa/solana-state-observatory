# Solana State Observatory — Snapshot

Generated **2026-11-09T01:58:34Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.71K tx/s |
| Slot time (sampled) | 0.2141 s |
| Epoch progress | 34.61% |
| Active validators | 661 |
| Delinquent stake | 0.1444% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 87.82 USD | -1.38% |
| DeFi TVL | 5.14B USD | — |
| Stablecoin supply | 14.71B USD | — |
| DEX volume | 995.30M USD | 8.49% |
| Protocol fees | 8.38M USD | 4.81% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | DEX volume | 995.30MUSD | -45.96% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.05M SOL | 7% |
| `he1iusun…PauBtk` | 16.72M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 13.02M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.28M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.55M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.55M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.22M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.78M SOL | 7% |

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
