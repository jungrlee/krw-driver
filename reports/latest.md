# USD/KRW Driver Note — 2026-10-27

USD/KRW rose 0.23% to 1,324.8 on 27 Oct 2026. The driver model attributes Dollar bloc +0.20pp, Korean equities -0.08pp, Oil -0.02pp; +0.13pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Dollar bloc**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,324.8 |
| 1-day change | +0.23% (z = +0.4 vs 60d vol) |
| 20d / 60d moving average | 1,337.9 / 1,365.7 |
| 1-month range | 1,321.8 – 1,360.6 |
| 3-month range | 1,321.8 – 1,435.7 |
| 20d realised vol (annualised) | 7.0% |

![USD/KRW](img/2026-10-27_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.20pp | +1.75pp |
| Korean equities | -0.08pp | +0.64pp |
| Oil | -0.02pp | +0.47pp |
| Unexplained (KRW-specific) | +0.13pp | -4.76pp |
| **Actual USD/KRW move** | **+0.23%** | **-1.91%** |

![Attribution](img/2026-10-27_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.976 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.465 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.025 | -0.058 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.026 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-27_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,967 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
