# USD/KRW Driver Note — 2026-10-19

USD/KRW fell 0.56% to 1,333.4 on 19 Oct 2026. The driver model attributes Dollar bloc -0.15pp, Korean equities -0.04pp, Oil +0.12pp; -0.48pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,333.4 |
| 1-day change | -0.56% (z = -0.9 vs 60d vol) |
| 20d / 60d moving average | 1,348.7 / 1,377.2 |
| 1-month range | 1,333.4 – 1,384.9 |
| 3-month range | 1,333.4 – 1,475.6 |
| 20d realised vol (annualised) | 10.5% |

![USD/KRW](img/2026-10-19_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.15pp | +2.90pp |
| Korean equities | -0.04pp | +0.37pp |
| Oil | +0.12pp | +0.19pp |
| Unexplained (KRW-specific) | -0.48pp | -4.36pp |
| **Actual USD/KRW move** | **-0.56%** | **-0.91%** |

![Attribution](img/2026-10-19_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.992 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.432 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.024 | -0.059 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.031 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-19_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,961 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
