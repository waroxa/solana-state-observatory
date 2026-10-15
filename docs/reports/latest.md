# Solana State Observatory — Snapshot

Generated **2026-10-15T22:40:28Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.85K tx/s |
| Slot time (sampled) | 0.2158 s |
| Epoch progress | 81.35% |
| Active validators | 671 |
| Delinquent stake | 0.0236% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 105.84 USD | 1.34% |
| DeFi TVL | 6.04B USD | — |
| Stablecoin supply | 15.85B USD | — |
| DEX volume | 2.12B USD | -15.08% |
| Protocol fees | 10.68M USD | -10.37% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | Delinquent stake | 0.02% | +148.42% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.56M SOL | 7% |
| `he1iusun…PauBtk` | 15.48M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.34M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.13M SOL | 0% |
| `CatzoSMU…gZDiqb` | 10.78M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.41M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.74M SOL | 7% |

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
