"""Tests on synthetic data with known betas (no network needed)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from krwmon import data, model
from krwmon.run import build

TRUE = {"DXY": 0.6, "USDCNH": 0.5, "KOSPI": -0.15, "UST2Y": 0.004, "BRENT": 0.02}


def synthetic_levels(n: int = 900, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2021-01-01", periods=n)
    chg = pd.DataFrame(
        {
            "DXY": rng.normal(0, 0.4, n),
            "USDCNH": rng.normal(0, 0.3, n),
            "KOSPI": rng.normal(0, 1.1, n),
            "UST2Y": rng.normal(0, 6.0, n),  # bp
            "BRENT": rng.normal(0, 2.0, n),
        },
        index=idx,
    )
    y = sum(TRUE[c] * chg[c] for c in TRUE) + rng.normal(0, 0.25, n)
    lv = pd.DataFrame(index=idx)
    lv["USDKRW"] = 1300 * np.exp(np.cumsum(y) / 100)
    for c in ("DXY", "USDCNH", "KOSPI", "BRENT"):
        lv[c] = 100 * np.exp(np.cumsum(chg[c]) / 100)
    lv["UST2Y"] = 4.0 + np.cumsum(chg["UST2Y"]) / 100
    return lv


def test_full_sample_recovers_true_betas():
    ch = data.to_changes(synthetic_levels())
    y, X = model.split_xy(ch)
    table, r2 = model.full_sample_hac(y, X)
    for c, b in TRUE.items():
        assert table.loc[c, "beta"] == pytest.approx(b, abs=0.05 if c != "UST2Y" else 0.002)
    assert r2 > 0.5


def test_attribution_has_no_look_ahead():
    """Truncation test: day t's attribution must not change if data after t is deleted."""
    lv = synthetic_levels()
    ch = data.to_changes(lv)
    y, X = model.split_xy(ch)
    full = model.attribute(y, X, model.rolling_betas(y, X, 120))

    t = ch.index[500]
    ch_cut = ch.loc[:t]
    y2, X2 = model.split_xy(ch_cut)
    cut = model.attribute(y2, X2, model.rolling_betas(y2, X2, 120))
    pd.testing.assert_series_equal(full.loc[t], cut.loc[t], check_names=False)


def test_contributions_add_up():
    ch = data.to_changes(synthetic_levels())
    y, X = model.split_xy(ch)
    att = model.attribute(y, X, model.rolling_betas(y, X, 120))
    g = model.group_contributions(att)
    # driver buckets + unexplained reproduce the actual move exactly
    assert np.allclose(g.sum(axis=1), att["actual"], atol=1e-9)


def test_calendar_alignment_drops_holidays():
    lv = synthetic_levels(300)
    lv.iloc[10, lv.columns.get_loc("KOSPI")] = np.nan  # a Korean holiday
    ch = data.to_changes(lv)
    assert lv.index[10] not in ch.index  # no 0% day invented


def test_end_to_end_writes_note(tmp_path):
    path = build(synthetic_levels(), 120, tmp_path)
    text = path.read_text(encoding="utf-8")
    assert "USD/KRW Driver Note" in text and "Out-of-sample" in text
    assert (tmp_path / "latest.md").exists()
    assert len(list((tmp_path / "img").glob("*.png"))) == 3
