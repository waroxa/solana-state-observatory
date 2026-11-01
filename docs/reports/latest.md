# Solana State Observatory — Snapshot

Generated **2026-11-01T02:38:28Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 1.37K tx/s |
| Slot time (sampled) | 0.2135 s |
| Epoch progress | 90.45% |
| Active validators | 665 |
| Delinquent stake | 0.8474% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 95.34 USD | -1.45% |
| DeFi TVL | 5.44B USD | — |
| Stablecoin supply | 15.16B USD | — |
| DEX volume | 1.44B USD | -31.85% |
| Protocol fees | 8.59M USD | -23.57% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| CRITICAL | Delinquent stake | 0.85% | +220.08% |
| WARNING | DEX volume | 1.44BUSD | -27.74% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.02M SOL | 7% |
| `he1iusun…PauBtk` | 16.69M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.93M SOL | 0% |
| `8GbwASqd…GJF8iD` | 10.43M SOL | 0% |
| `CatzoSMU…gZDiqb` | 9.65M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.45M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.23M SOL | 7% |
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
