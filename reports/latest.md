# USD/KRW Driver Note — 2026-11-19

USD/KRW fell 0.20% to 1,330.4 on 19 Nov 2026. The driver model attributes Dollar bloc +0.26pp, Korean equities -0.06pp, Oil +0.01pp; -0.41pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,330.4 |
| 1-day change | -0.20% (z = -0.3 vs 60d vol) |
| 20d / 60d moving average | 1,336.9 / 1,346.9 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,384.9 |
| 20d realised vol (annualised) | 10.4% |

![USD/KRW](img/2026-11-19_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.26pp | +1.71pp |
| Korean equities | -0.06pp | +0.25pp |
| Oil | +0.01pp | -0.13pp |
| Unexplained (KRW-specific) | -0.41pp | -1.46pp |
| **Actual USD/KRW move** | **-0.20%** | **+0.36%** |

![Attribution](img/2026-11-19_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.758 | +0.514 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.799 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.043 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.005 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-19_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,984 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
