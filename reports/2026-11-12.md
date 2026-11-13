# USD/KRW Driver Note — 2026-11-12

USD/KRW fell 0.42% to 1,336.3 on 12 Nov 2026. The driver model attributes Dollar bloc +0.58pp, Korean equities +0.02pp, Oil -0.00pp; -1.03pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,336.3 |
| 1-day change | -0.42% (z = -0.7 vs 60d vol) |
| 20d / 60d moving average | 1,336.3 / 1,351.1 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,414.7 |
| 20d realised vol (annualised) | 10.7% |

![USD/KRW](img/2026-11-12_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.58pp | +0.31pp |
| Korean equities | +0.02pp | +0.10pp |
| Oil | -0.00pp | -0.06pp |
| Unexplained (KRW-specific) | -1.03pp | -0.59pp |
| **Actual USD/KRW move** | **-0.42%** | **-0.23%** |

![Attribution](img/2026-11-12_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.785 | +0.515 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.417 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.041 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.006 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-12_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,979 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
