# Solana State Observatory — Snapshot

Generated **2026-10-09T07:23:29Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 4.02K tx/s |
| Slot time (sampled) | 0.2668 s |
| Epoch progress | 77.32% |
| Active validators | 673 |
| Delinquent stake | 0.0073% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 110.43 USD | -4.54% |
| DeFi TVL | 6.25B USD | — |
| Stablecoin supply | 16.04B USD | — |
| DEX volume | 2.44B USD | 10.65% |
| Protocol fees | 14.30M USD | 4.00% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| — | No anomaly detected | — | — |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 17.82M SOL | 7% |
| `he1iusun…PauBtk` | 15.94M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.32M SOL | 0% |
| `8GbwASqd…GJF8iD` | 11.22M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.08M SOL | 5% |
| `51JBzSTU…zgUNAm` | 9.27M SOL | 10% |
| `26pV97Ce…c53dJx` | 9.26M SOL | 7% |
| `9QU2QSxh…aM29mF` | 7.51M SOL | 7% |

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
