# USD/KRW Driver Note — 2026-10-30

USD/KRW fell 0.18% to 1,338.0 on 30 Oct 2026. The driver model attributes Dollar bloc -0.10pp, Korean equities +0.09pp, Oil -0.01pp; -0.15pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,338.0 |
| 1-day change | -0.18% (z = -0.3 vs 60d vol) |
| 20d / 60d moving average | 1,334.7 / 1,361.3 |
| 1-month range | 1,321.8 – 1,360.6 |
| 3-month range | 1,321.8 – 1,428.4 |
| 20d realised vol (annualised) | 7.4% |

![USD/KRW](img/2026-10-30_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.10pp | +1.05pp |
| Korean equities | +0.09pp | +0.48pp |
| Oil | -0.01pp | +0.37pp |
| Unexplained (KRW-specific) | -0.15pp | -2.83pp |
| **Actual USD/KRW move** | **-0.18%** | **-0.93%** |

![Attribution](img/2026-10-30_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.971 | +0.516 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.527 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.026 | -0.058 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.028 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-30_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,970 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
