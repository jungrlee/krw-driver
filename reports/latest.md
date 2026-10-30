# USD/KRW Driver Note — 2026-10-29

USD/KRW rose 1.01% to 1,340.3 on 29 Oct 2026. The driver model attributes Dollar bloc -0.11pp, Korean equities +0.03pp, Oil +0.03pp; +1.06pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,340.3 |
| 1-day change | +1.01% (z = +1.7 vs 60d vol) |
| 20d / 60d moving average | 1,335.8 / 1,362.7 |
| 1-month range | 1,321.8 – 1,360.6 |
| 3-month range | 1,321.8 – 1,428.5 |
| 20d realised vol (annualised) | 7.5% |

![USD/KRW](img/2026-10-29_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.11pp | +1.41pp |
| Korean equities | +0.03pp | +0.40pp |
| Oil | +0.03pp | +0.32pp |
| Unexplained (KRW-specific) | +1.06pp | -3.56pp |
| **Actual USD/KRW move** | **+1.01%** | **-1.42%** |

![Attribution](img/2026-10-29_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.969 | +0.516 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.505 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.026 | -0.058 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.027 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-29_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,969 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
