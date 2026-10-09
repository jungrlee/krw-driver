# USD/KRW Driver Monitor

**What moved the won today, and how much of it can we explain?**

A small Python tool that breaks each day's USD/KRW move into its drivers (the US dollar, the Chinese yuan, Korean equities, US rates, oil) and writes a one-page desk note automatically: key levels, attribution, current sensitivities, and an honest check of how much the model actually explains.

```
USD/KRW rose 0.62% to 1,4xx.x. The driver model attributes Dollar bloc +0.41pp,
Korean equities +0.12pp, Rates +0.03pp, Oil +0.01pp; +0.05pp is unexplained
(KRW-specific flows or positioning). Largest single bucket: Dollar bloc.
```
*(Illustrative format. Run the tool to see the current note in [`reports/latest.md`](reports/latest.md).)*

---

## What the note contains

| Section | What it answers |
|---|---|
| **Headline** | How much did USD/KRW move, and which bucket drove it? |
| **Key levels** | Last, 20d/60d moving averages, 1m and 3m ranges, 20d realised vol, size of the move vs recent volatility |
| **Attribution** | Each driver's contribution, last day and cumulative over 20 days, plus a stacked chart |
| **Sensitivities** | Rolling betas now vs full-sample betas (Newey-West t-stats) |
| **Foreign flows** *(optional)* | KOSPI foreign net buying, last 5 days |
| **How reliable is this?** | Out-of-sample explained share, sign hit rate, in-sample R² for comparison |

## Method

1. **Data.** Daily closes from Yahoo Finance (USD/KRW, DXY, USD/CNH, KOSPI, Brent) and FRED (US 2y Treasury yield). Optional: the Korea 3y KTB yield from the Bank of Korea ECOS API, and KOSPI foreign flows from KRX via `pykrx`.
2. **Alignment before returns.** Series are aligned on common trading dates *before* computing changes, so every daily change covers the same calendar interval. Holidays are dropped, not filled with 0% moves (which would understate volatility and distort betas).
3. **Changes.** Prices become log returns in %; yields become changes in basis points.
4. **Rolling regression.** ΔUSD/KRW is regressed on the drivers over a rolling 120-day window, so sensitivities can drift as regimes change.
5. **Point-in-time attribution.** Day *t*'s move is attributed using betas estimated **through day t−1 only**. A coefficient never "knows" the move it is explaining. A unit test enforces this: deleting all data after *t* must not change day *t*'s attribution.
6. **Honest evaluation.** The note reports the out-of-sample explained share of daily moves next to the in-sample R², which is optimistic by construction.

**Expected signs** (a sanity check on the output): DXY and USD/CNH positive (a broadly stronger dollar or weaker yuan lifts USD/KRW); KOSPI negative (risk-on and foreign equity inflows strengthen the won); US 2y positive on balance (wider rate gap supports the dollar).

## Limitations, stated up front

- **Attribution, not forecasting.** Same-day drivers explain same-day moves. Nothing here is a trading signal.
- **Asynchronous closes.** KOSPI closes in Seoul; DXY and Treasuries in New York; Yahoo's USD/KRW close is not the onshore 15:30 fix. Single-day attribution is blurred, so 20-day totals deserve more weight than any one day.
- **Collinear drivers.** DXY and USD/CNH move together, so their individual betas are less stable than their combined "Dollar bloc" contribution. That is why the headline reports buckets.
- **Unstable betas.** Sensitivities change with regimes; the rolling window trades noise (short) against staleness (long).
- **The residual is not "noise".** Onshore-specific drivers (exporter dollar sales, NPS hedging, BoK smoothing, positioning) live in the unexplained bucket.

## Quickstart

```bash
git clone https://github.com/jungrlee/krw-driver-monitor.git
cd krw-driver-monitor
pip install -r requirements.txt

python -m krwmon                 # download data, write reports/latest.md
python -m krwmon --flows         # add the KOSPI foreign-flows panel (needs pykrx)
python -m krwmon --window 60     # faster-adapting betas
python -m krwmon --offline       # re-run on cached data
```

Optional Korean rates driver: get a free key at [ecos.bok.or.kr](https://ecos.bok.or.kr) and set `ECOS_API_KEY`.

Run the tests (synthetic data, no network):

```bash
pytest -q
```

The tests check that known betas are recovered, that attribution has **no look-ahead** (truncation test), that contributions add up to the actual move, that holidays are not filled with 0% days, and that the full pipeline writes a note.

## Automation

`.github/workflows/daily.yml` runs the monitor every weekday at 07:45 KST and commits the new note to `reports/`. Enable Actions on the repo (and allow workflows to write to the repository) to turn it on.

## Project structure

```
krwmon/
  config.py   series, tickers, groups, palette
  data.py     downloads + calendar alignment + changes
  model.py    rolling betas, point-in-time attribution, evaluation, key levels
  report.py   charts + Markdown desk note
  run.py      command-line entry point
tests/        synthetic-data tests (incl. no-look-ahead check)
reports/      generated notes and charts
```

## Roadmap

- Onshore vs offshore: NDF-implied rate vs onshore spot spread
- FX swap points converted to an implied KRW yield vs CD/KOFR (hedging cost for Korean investors abroad)
- Intraday attribution around the Seoul close to reduce the asynchronous-close problem

## Author

Jung Ryul Lee · FMBA (Finance & Business Analytics), SKK Graduate School of Business · [github.com/jungrlee](https://github.com/jungrlee)

*For research and educational use. Not investment advice.*
