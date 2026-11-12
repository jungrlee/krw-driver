# USD/KRW Driver Note — 2026-11-11

USD/KRW fell 0.14% to 1,341.9 on 11 Nov 2026. The driver model attributes Dollar bloc +0.54pp, Korean equities -0.10pp, Oil +0.00pp; -0.59pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,341.9 |
| 1-day change | -0.14% (z = -0.2 vs 60d vol) |
| 20d / 60d moving average | 1,336.4 / 1,352.0 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,415.4 |
| 20d realised vol (annualised) | 10.6% |

![USD/KRW](img/2026-11-11_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.54pp | +0.09pp |
| Korean equities | -0.10pp | +0.29pp |
| Oil | +0.00pp | -0.04pp |
| Unexplained (KRW-specific) | -0.59pp | -0.22pp |
| **Actual USD/KRW move** | **-0.14%** | **+0.12%** |

![Attribution](img/2026-11-11_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.881 | +0.516 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.510 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.038 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.002 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-11_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,978 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
