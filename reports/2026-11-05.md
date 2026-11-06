# USD/KRW Driver Note — 2026-11-05

USD/KRW fell 0.21% to 1,340.1 on 05 Nov 2026. The driver model attributes Dollar bloc -0.37pp, Korean equities +0.16pp, Oil -0.08pp; +0.08pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Dollar bloc**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,340.1 |
| 1-day change | -0.21% (z = -0.3 vs 60d vol) |
| 20d / 60d moving average | 1,334.1 / 1,356.3 |
| 1-month range | 1,321.8 – 1,344.8 |
| 3-month range | 1,321.8 – 1,417.3 |
| 20d realised vol (annualised) | 8.5% |

![USD/KRW](img/2026-11-05_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.37pp | -0.11pp |
| Korean equities | +0.16pp | +0.66pp |
| Oil | -0.08pp | +0.10pp |
| Unexplained (KRW-specific) | +0.08pp | -0.62pp |
| **Actual USD/KRW move** | **-0.21%** | **+0.02%** |

![Attribution](img/2026-11-05_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.948 | +0.516 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.640 | +0.409 | +6.9 |
| KOSPI index (% per 1%) | -0.031 | -0.059 | -6.6 |
| Brent crude (front month) (% per 1%) | +0.008 | -0.005 | -0.7 |

![Rolling betas](img/2026-11-05_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,974 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
