# USD/KRW Driver Note — 2026-11-09

USD/KRW rose 0.47% to 1,362.7 on 09 Nov 2026. The driver model attributes Dollar bloc +0.76pp, Korean equities +0.03pp, Oil -0.00pp; -0.32pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Dollar bloc**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,362.7 |
| 1-day change | +0.47% (z = +0.7 vs 60d vol) |
| 20d / 60d moving average | 1,335.9 / 1,354.4 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,416.8 |
| 20d realised vol (annualised) | 9.6% |

![USD/KRW](img/2026-11-09_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.76pp | +0.11pp |
| Korean equities | +0.03pp | +0.71pp |
| Oil | -0.00pp | -0.00pp |
| Unexplained (KRW-specific) | -0.32pp | +0.80pp |
| **Actual USD/KRW move** | **+0.47%** | **+1.62%** |

![Attribution](img/2026-11-09_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.837 | +0.516 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.531 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.035 | -0.059 | -6.7 |
| Brent crude (front month) (% per 1%) | -0.002 | -0.005 | -0.7 |

![Rolling betas](img/2026-11-09_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,976 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
