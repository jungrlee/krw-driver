# USD/KRW Driver Note — 2026-11-18

USD/KRW fell 0.20% to 1,333.0 on 18 Nov 2026. The driver model attributes Dollar bloc -0.06pp, Korean equities -0.08pp, Oil -0.01pp; -0.05pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Korean equities**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,333.0 |
| 1-day change | -0.20% (z = -0.3 vs 60d vol) |
| 20d / 60d moving average | 1,336.7 / 1,347.7 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,385.0 |
| 20d realised vol (annualised) | 10.4% |

![USD/KRW](img/2026-11-18_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.06pp | +1.49pp |
| Korean equities | -0.08pp | +0.40pp |
| Oil | -0.01pp | -0.14pp |
| Unexplained (KRW-specific) | -0.05pp | -1.07pp |
| **Actual USD/KRW move** | **-0.20%** | **+0.68%** |

![Attribution](img/2026-11-18_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.781 | +0.514 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.552 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.042 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.007 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-18_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,983 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
