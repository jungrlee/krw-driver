# USD/KRW Driver Note — 2026-10-16

USD/KRW rose 0.12% to 1,340.9 on 16 Oct 2026. The driver model attributes Dollar bloc -0.54pp, Korean equities -0.05pp, Oil -0.00pp; +0.72pp is unexplained (KRW-specific flows or positioning). Largest single bucket: **Unexplained (KRW-specific)**.

## Key levels

| Level | Value |
|---|---|
| Last | 1,340.9 |
| 1-day change | +0.12% (z = +0.2 vs 60d vol) |
| 20d / 60d moving average | 1,351.2 / 1,379.3 |
| 1-month range | 1,334.1 – 1,384.9 |
| 3-month range | 1,334.1 – 1,479.7 |
| 20d realised vol (annualised) | 10.6% |

![USD/KRW](img/2026-10-16_price.png)

## Attribution

| Bucket | Last day | Last 20 days (cumulative) |
|---|---|---|
| Dollar bloc | -0.54pp | +3.44pp |
| Korean equities | -0.05pp | +0.44pp |
| Oil | -0.00pp | +0.09pp |
| Unexplained (KRW-specific) | +0.72pp | -4.25pp |
| **Actual USD/KRW move** | **+0.12%** | **-0.27%** |

![Attribution](img/2026-10-16_attribution.png)

## Current sensitivities

Rolling 120-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.

| Driver | Rolling beta (now) | Full-sample beta | t-stat |
|---|---|---|---|
| US Dollar Index (% per 1%) | +0.984 | +0.515 | +12.6 |
| USD/CNH (offshore yuan) (% per 1%) | -0.421 | +0.412 | +6.9 |
| KOSPI index (% per 1%) | -0.024 | -0.059 | -6.5 |
| Brent crude (front month) (% per 1%) | +0.032 | -0.004 | -0.6 |

![Rolling betas](img/2026-10-16_betas.png)

## How reliable is this?

- Out-of-sample explained share of daily moves: **27%** (betas estimated through the previous day only; 1,960 days).
- In-sample R² for comparison: 29% — optimistic by construction.
- Sign of the move matched on **69%** of days.
- This is attribution, not a forecast: same-day drivers explain same-day moves.
- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals with more confidence than single days.
