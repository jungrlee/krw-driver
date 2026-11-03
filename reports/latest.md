# USD/KRW Driver Note — 2026-11-02

USD/KRW fell 0.94% to 1,325.5 on 02 Nov 2026. The driver model attributes Dollar bloc -0.15pp, Korean equities -0.06pp, Oil +0.07pp; -0.79pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,325.5 |
| 1-day change | -0.94% (z = -1.6 vs 60d vol) |
| 20d / 60d moving average | 1,333.9 / 1,359.9 |
| 1-month range | 1,321.8 – 1,343.8 |
| 3-month range | 1,321.8 – 1,422.3 |
| 20d realised vol (annualised) | 6.7% |

![USD/KRW](img/2026-11-02_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.15pp | +0.82pp |
| Korean equities | -0.06pp | +0.49pp |
| Oil | +0.07pp | +0.41pp |
| Unexplained (KRW-specific) | -0.79pp | -4.06pp |
| **Actual USD/KRW move** | **-0.94%** | **-2.34%** |

![Attribution](img/2026-11-02_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.984 | +0.516 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.546 | +0.411 | +6.9 |
| KOSPI index (% per 1%) | -0.026 | -0.058 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.026 | -0.004 | -0.6 |

![Rolling betas](img/2026-11-02_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,971 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
