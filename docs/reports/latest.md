# Solana State Observatory — Snapshot

Generated **2026-08-27T03:34:01Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.20K tx/s |
| Slot time (sampled) | 0.3666 s |
| Epoch progress | 18.34% |
| Active validators | 686 |
| Delinquent stake | 0.0224% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 101.47 USD | 4.66% |
| DeFi TVL | 5.76B USD | — |
| Stablecoin supply | 15.82B USD | — |
| DEX volume | 2.49B USD | -15.10% |
| Protocol fees | 13.83M USD | 4.52% |

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
