"""End-to-end run: fetch -> changes -> rolling model -> attribution -> note."""

from __future__ import annotations

import argparse
import warnings
from pathlib import Path

import pandas as pd

from . import data, model, report
from .config import DEFAULT_START, DEFAULT_WINDOW, TARGET


def build(levels: pd.DataFrame, window: int, out_dir: Path, flows: pd.Series | None = None) -> Path:
    changes = data.to_changes(levels)
    if len(changes) < window + 30:
        raise ValueError(f"Only {len(changes)} aligned days; need more than window={window} + 30")

    y, X = model.split_xy(changes)
    betas = model.rolling_betas(y, X, window)
    att = model.attribute(y, X, betas)
    groups = model.group_contributions(att)
    hac_table, full_r2 = model.full_sample_hac(y, X)
    ev = model.evaluate(att, full_r2)

    target_level = levels[TARGET].dropna()
    lv = model.key_levels(target_level.loc[: att.index[-1]])

    date = att.index[-1]
    img = out_dir / "img"
    img.mkdir(parents=True, exist_ok=True)
    report.chart_price(target_level.loc[:date], img / f"{date:%Y-%m-%d}_price.png")
    report.chart_betas(betas, img / f"{date:%Y-%m-%d}_betas.png")
    report.chart_attribution(att, img / f"{date:%Y-%m-%d}_attribution.png")

    att.to_csv(out_dir / "attribution_history.csv", float_format="%.5f")
    return report.write_note(out_dir, lv, att, groups, hac_table, ev, window, betas.iloc[-1], flows)


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="USD/KRW driver monitor: daily attribution note")
    p.add_argument("--start", default=DEFAULT_START, help="first date to download (YYYY-MM-DD)")
    p.add_argument("--window", type=int, default=DEFAULT_WINDOW, help="rolling regression window (days)")
    p.add_argument("--out", default="reports", help="output folder for the note and charts")
    p.add_argument("--cache", default="data", help="folder for the cached raw levels")
    p.add_argument("--offline", action="store_true", help="use cached data instead of downloading")
    p.add_argument("--flows", action="store_true", help="add KOSPI foreign net-buying panel (needs pykrx)")
    a = p.parse_args(argv)

    levels = data.load_levels(a.start, Path(a.cache), offline=a.offline)
    flows = data.fetch_foreign_flows(a.start) if a.flows else None
    if a.flows and flows is None:
        warnings.warn("Flows requested but unavailable (install pykrx or check KRX access)")
    path = build(levels, a.window, Path(a.out), flows)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
