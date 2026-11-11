# USD/KRW Driver Note — 2026-11-10

USD/KRW fell 1.39% to 1,343.8 on 10 Nov 2026. The driver model attributes Dollar bloc -0.51pp, Korean equities -0.15pp, Oil +0.01pp; -0.75pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,343.8 |
| 1-day change | -1.39% (z = -2.1 vs 60d vol) |
| 20d / 60d moving average | 1,336.4 / 1,353.2 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,416.8 |
| 20d realised vol (annualised) | 10.7% |

![USD/KRW](img/2026-11-10_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.51pp | -0.87pp |
| Korean equities | -0.15pp | +0.40pp |
| Oil | +0.01pp | -0.07pp |
| Unexplained (KRW-specific) | -0.75pp | +1.27pp |
| **Actual USD/KRW move** | **-1.39%** | **+0.73%** |

![Attribution](img/2026-11-10_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.915 | +0.517 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.602 | +0.409 | +6.9 |
| KOSPI index (% per 1%) | -0.038 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.001 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-10_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,977 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
