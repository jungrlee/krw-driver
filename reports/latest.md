# USD/KRW Driver Note — 2026-11-20

USD/KRW rose 0.33% to 1,334.8 on 20 Nov 2026. The driver model attributes Dollar bloc +0.04pp, Korean equities +0.23pp, Oil -0.00pp; +0.06pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Korean equities**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,334.8 |
| 1-day change | +0.33% (z = +0.5 vs 60d vol) |
| 20d / 60d moving average | 1,337.3 / 1,346.1 |
| 1-month range | 1,321.8 – 1,362.7 |
| 3-month range | 1,321.8 – 1,384.9 |
| 20d realised vol (annualised) | 10.5% |

![USD/KRW](img/2026-11-20_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | +0.04pp | +1.92pp |
| Korean equities | +0.23pp | +0.49pp |
| Oil | -0.00pp | -0.24pp |
| Unexplained (KRW-specific) | +0.06pp | -1.50pp |
| **Actual USD/KRW move** | **+0.33%** | **+0.66%** |

![Attribution](img/2026-11-20_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.757 | +0.514 | +12.7 |
| USD/CNH (offshore yuan) (% per 1%) | -0.814 | +0.410 | +6.9 |
| KOSPI index (% per 1%) | -0.043 | -0.060 | -6.8 |
| Brent crude (front month) (% per 1%) | -0.005 | -0.004 | -0.7 |

![Rolling betas](img/2026-11-20_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,985 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
