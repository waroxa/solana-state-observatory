# Solana State Observatory — Snapshot

Generated **2026-10-23T04:47:30Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.58K tx/s |
| Slot time (sampled) | 0.2118 s |
| Epoch progress | 53.79% |
| Active validators | 656 |
| Delinquent stake | 0.2954% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 103.88 USD | -1.41% |
| DeFi TVL | 5.89B USD | — |
| Stablecoin supply | 15.64B USD | — |
| DEX volume | 2.12B USD | -6.75% |
| Protocol fees | 11.21M USD | -5.21% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | TPS | 1.58Ktx/s | -67.34% |
| CRITICAL | Delinquent stake | 0.30% | +6769.77% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.13M SOL | 7% |
| `he1iusun…PauBtk` | 15.97M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.56M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.94M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.73M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.48M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.24M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.80M SOL | 7% |

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
