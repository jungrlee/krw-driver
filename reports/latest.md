# USD/KRW Driver Note — 2026-11-26

USD/KRW rose 0.02% to 1,343.0 on 26 Nov 2026. The driver model attributes Dollar bloc -0.09pp, Korean equities -0.01pp, Oil -0.01pp; +0.14pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,343.0 |
| 1-day change | +0.02% (z = +0.0 vs 60d vol) |
| 20d / 60d moving average | 1,340.2 / 1,344.4 |
| 1-month range | 1,325.5 – 1,362.7 |
| 3-month range | 1,321.8 – 1,384.9 |
| 20d realised vol (annualised) | 10.1% |

![USD/KRW](img/2026-11-26_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.09pp | +1.14pp |
| Korean equities | -0.01pp | +0.82pp |
| Oil | -0.01pp | -0.31pp |
| Unexplained (KRW-specific) | +0.14pp | -1.45pp |
| **Actual USD/KRW move** | **+0.02%** | **+0.20%** |

![Attribution](img/2026-11-26_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.670 | +0.513 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.561 | +0.411 | +6.9 |
| KOSPI index (% per 1%) | -0.048 | -0.060 | -7.0 |
| Brent crude (front month) (% per 1%) | -0.004 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-26_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,989 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
