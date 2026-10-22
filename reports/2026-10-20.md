# USD/KRW Driver Note — 2026-10-20

USD/KRW fell 0.26% to 1,330.0 on 20 Oct 2026. The driver model attributes Dollar bloc +0.14pp, Korean equities +0.09pp, Oil -0.01pp; -0.48pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,330.0 |
| 1-day change | -0.26% (z = -0.4 vs 60d vol) |
| 20d / 60d moving average | 1,346.5 / 1,375.0 |
| 1-month range | 1,330.0 – 1,373.7 |
| 3-month range | 1,330.0 – 1,474.0 |
| 20d realised vol (annualised) | 10.3% |

![USD/KRW](img/2026-10-20_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.14pp | +2.83pp |
| Korean equities | +0.09pp | +0.51pp |
| Oil | -0.01pp | +0.13pp |
| Unexplained (KRW-specific) | -0.48pp | -5.96pp |
| **Actual USD/KRW move** | **-0.26%** | **-2.49%** |

![Attribution](img/2026-10-20_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.997 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.469 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.024 | -0.059 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.031 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-20_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,962 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
