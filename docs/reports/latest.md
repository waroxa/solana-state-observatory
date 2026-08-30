# Solana State Observatory — Snapshot

Generated **2026-08-30T01:40:23Z** · mainnet-beta · health score **100/100 (healthy)**

> This is an automatically generated diagnostic report, not financial advice. A missing source is shown as unavailable rather than silently replaced with stale data.

## Executive signal

| Network | Current |
|---|---:|
| RPC health | ok |
| Throughput (sampled) | 3.84K tx/s |
| Slot time (sampled) | 0.3184 s |
| Epoch progress | 89.92% |
| Active validators | 687 |
| Delinquent stake | 0.0088% |

## Economic pulse

| Metric | Current | 24h change |
|---|---:|---:|
| SOL price | 105.25 USD | 1.07% |
| DeFi TVL | 5.89B USD | — |
| Stablecoin supply | 15.90B USD | — |
| DEX volume | 1.81B USD | -29.96% |
| Protocol fees | 13.55M USD | -13.85% |

## Anomaly register

| Severity | Metric | Observation | vs rolling baseline |
|---|---|---:|---:|
| WARNING | SOL price | 105.25USD | +8.15% |
| WARNING | DEX volume | 1.81BUSD | -38.47% |

## Validator concentration lens

| Vote account | Activated stake | Commission |
|---|---:|---:|
| `CcaHc2L4…BzoTN1` | 16.99M SOL | 7% |
| `he1iusun…PauBtk` | 16.04M SOL | 0% |
| `3N7s9zXM…eWiD5g` | 12.39M SOL | 0% |
| `CatzoSMU…gZDiqb` | 11.46M SOL | 5% |
| `26pV97Ce…c53dJx` | 9.29M SOL | 7% |
| `8GbwASqd…GJF8iD` | 9.08M SOL | 0% |
| `51JBzSTU…zgUNAm` | 9.00M SOL | 10% |
| `CvSb7wdQ…aKwycB` | 7.29M SOL | 5% |

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
