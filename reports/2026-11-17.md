# USD/KRW Driver Note — 2026-11-17

USD/KRW rose 0.18% to 1,335.7 on 17 Nov 2026. The driver model attributes Dollar bloc +0.15pp, Korean equities +0.11pp, Oil +0.02pp; -0.10pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Dollar bloc**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,335.7 |
| 1-day change | +0.18% (z = +0.3 vs 60d vol) |
| 20d / 60d moving average | 1,336.2 / 1,348.6 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,390.8 |
| 20d realised vol (annualised) | 10.5% |

![USD/KRW](img/2026-11-17_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.15pp | +1.40pp |
| Korean equities | +0.11pp | +0.40pp |
| Oil | +0.02pp | -0.15pp |
| Unexplained (KRW-specific) | -0.10pp | -1.22pp |
| **Actual USD/KRW move** | **+0.18%** | **+0.43%** |

![Attribution](img/2026-11-17_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.787 | +0.514 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.541 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.041 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.007 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-17_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,982 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
