# USD/KRW Driver Note — 2026-10-23

USD/KRW rose 0.03% to 1,326.0 on 23 Oct 2026. The driver model attributes Dollar bloc -0.17pp, Korean equities -0.01pp, Oil +0.11pp; +0.09pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Dollar bloc**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,326.0 |
| 1-day change | +0.03% (z = +0.0 vs 60d vol) |
| 20d / 60d moving average | 1,341.2 / 1,369.3 |
| 1-month range | 1,323.9 – 1,367.4 |
| 3-month range | 1,323.9 – 1,453.2 |
| 20d realised vol (annualised) | 7.6% |

![USD/KRW](img/2026-10-23_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.17pp | +1.79pp |
| Korean equities | -0.01pp | +0.65pp |
| Oil | +0.11pp | +0.31pp |
| Unexplained (KRW-specific) | +0.09pp | -7.09pp |
| **Actual USD/KRW move** | **+0.03%** | **-4.34%** |

![Attribution](img/2026-10-23_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.993 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.452 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.025 | -0.059 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.027 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-23_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,965 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
