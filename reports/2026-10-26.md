# USD/KRW Driver Note — 2026-10-26

USD/KRW fell 0.32% to 1,321.8 on 26 Oct 2026. The driver model attributes Dollar bloc +0.20pp, Korean equities +0.04pp, Oil +0.08pp; -0.64pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,321.8 |
| 1-day change | -0.32% (z = -0.5 vs 60d vol) |
| 20d / 60d moving average | 1,339.6 / 1,367.4 |
| 1-month range | 1,321.8 – 1,360.6 |
| 3-month range | 1,321.8 – 1,442.3 |
| 20d realised vol (annualised) | 7.1% |

![USD/KRW](img/2026-10-26_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.20pp | +1.72pp |
| Korean equities | +0.04pp | +0.69pp |
| Oil | +0.08pp | +0.46pp |
| Unexplained (KRW-specific) | -0.64pp | -6.72pp |
| **Actual USD/KRW move** | **-0.32%** | **-3.85%** |

![Attribution](img/2026-10-26_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.961 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.460 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.026 | -0.058 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.025 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-26_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,966 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
