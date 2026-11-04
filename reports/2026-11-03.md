# USD/KRW Driver Note — 2026-11-03

USD/KRW rose 1.44% to 1,344.8 on 03 Nov 2026. The driver model attributes Dollar bloc -0.02pp, Korean equities +0.10pp, Oil -0.30pp; +1.67pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,344.8 |
| 1-day change | +1.44% (z = +2.3 vs 60d vol) |
| 20d / 60d moving average | 1,333.9 / 1,358.7 |
| 1-month range | 1,321.8 – 1,344.8 |
| 3-month range | 1,321.8 – 1,422.3 |
| 20d realised vol (annualised) | 8.5% |

![USD/KRW](img/2026-11-03_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.02pp | +0.09pp |
| Korean equities | +0.10pp | +0.60pp |
| Oil | -0.30pp | +0.14pp |
| Unexplained (KRW-specific) | +1.67pp | -1.99pp |
| **Actual USD/KRW move** | **+1.44%** | **-1.17%** |

![Attribution](img/2026-11-03_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.970 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.711 | +0.409 | +6.9 |
| KOSPI index (% per 1%) | -0.030 | -0.059 | -6.6 |
| Brent crude (front month) (% per 1%) | +0.009 | -0.005 | -0.8 |

![Rolling betas](img/2026-11-03_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,972 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
