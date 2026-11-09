# USD/KRW Driver Note — 2026-11-06

USD/KRW rose 1.21% to 1,356.3 on 06 Nov 2026. The driver model attributes Dollar bloc -0.11pp, Korean equities +0.19pp, Oil +0.03pp; +1.09pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,356.3 |
| 1-day change | +1.21% (z = +1.9 vs 60d vol) |
| 20d / 60d moving average | 1,334.8 / 1,355.3 |
| 1-month range | 1,321.8 – 1,356.3 |
| 3-month range | 1,321.8 – 1,416.8 |
| 20d realised vol (annualised) | 9.5% |

![USD/KRW](img/2026-11-06_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.11pp | -0.67pp |
| Korean equities | +0.19pp | +0.78pp |
| Oil | +0.03pp | +0.15pp |
| Unexplained (KRW-specific) | +1.09pp | +1.03pp |
| **Actual USD/KRW move** | **+1.21%** | **+1.28%** |

![Attribution](img/2026-11-06_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.873 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.642 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.035 | -0.059 | -6.7 |
| Brent crude (front month) (% per 1%) | -0.002 | -0.005 | -0.7 |

![Rolling betas](img/2026-11-06_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,975 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
