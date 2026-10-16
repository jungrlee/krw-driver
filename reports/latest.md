# USD/KRW Driver Note — 2026-10-15

USD/KRW fell 0.07% to 1,339.3 on 15 Oct 2026. The driver model attributes Dollar bloc +0.37pp, Korean equities +0.21pp, Oil +0.01pp; -0.66pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,339.3 |
| 1-day change | -0.07% (z = -0.1 vs 60d vol) |
| 20d / 60d moving average | 1,353.2 / 1,381.5 |
| 1-month range | 1,334.1 – 1,384.9 |
| 3-month range | 1,334.1 – 1,479.7 |
| 20d realised vol (annualised) | 10.7% |

![USD/KRW](img/2026-10-15_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.37pp | +4.02pp |
| Korean equities | +0.21pp | +0.60pp |
| Oil | +0.01pp | +0.05pp |
| Unexplained (KRW-specific) | -0.66pp | -5.32pp |
| **Actual USD/KRW move** | **-0.07%** | **-0.66%** |

![Attribution](img/2026-10-15_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +1.034 | +0.516 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.467 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.024 | -0.059 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.032 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-15_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,959 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
