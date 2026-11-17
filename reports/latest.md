# USD/KRW Driver Note — 2026-11-16

USD/KRW fell 0.04% to 1,333.2 on 16 Nov 2026. The driver model attributes Dollar bloc +0.18pp, Korean equities +0.15pp, Oil -0.00pp; -0.37pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,333.2 |
| 1-day change | -0.04% (z = -0.1 vs 60d vol) |
| 20d / 60d moving average | 1,335.9 / 1,349.3 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,390.8 |
| 20d realised vol (annualised) | 10.6% |

![USD/KRW](img/2026-11-16_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.18pp | +1.38pp |
| Korean equities | +0.15pp | +0.38pp |
| Oil | -0.00pp | -0.19pp |
| Unexplained (KRW-specific) | -0.37pp | -1.59pp |
| **Actual USD/KRW move** | **-0.04%** | **-0.01%** |

![Attribution](img/2026-11-16_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.789 | +0.514 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.439 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.041 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.007 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-16_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,981 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
