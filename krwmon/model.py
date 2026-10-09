"""Driver model: rolling betas, point-in-time attribution, honest evaluation.

The attribution of day t uses betas estimated on data up to t-1 only, so no
coefficient ever "knows" the move it is explaining. This is an *attribution*
model (same-day drivers explain same-day USD/KRW moves), not a forecast.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS

from .config import ECOS_SERIES, HAC_LAGS, SERIES, TARGET


def split_xy(changes: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    y = changes[TARGET]
    X = changes.drop(columns=[TARGET])
    return y, X


def rolling_betas(y: pd.Series, X: pd.DataFrame, window: int) -> pd.DataFrame:
    """Row t = coefficients fitted on rows t-window+1 .. t (inclusive)."""
    res = RollingOLS(y, sm.add_constant(X), window=window).fit()
    return res.params


def attribute(y: pd.Series, X: pd.DataFrame, betas: pd.DataFrame) -> pd.DataFrame:
    """Split each day's move into driver contributions using betas from t-1."""
    b = betas.shift(1)  # point in time: estimated through yesterday
    contrib = X.mul(b[X.columns])
    fitted = contrib.sum(axis=1, min_count=1) + b["const"]
    out = contrib.copy()
    # KRW-specific move = everything the drivers do not explain (intercept included),
    # so driver contributions + residual add up exactly to the actual move.
    out["residual"] = y - contrib.sum(axis=1, min_count=1)
    out["fitted"] = fitted
    out["actual"] = y
    return out.dropna()


def group_contributions(att: pd.DataFrame) -> pd.DataFrame:
    """Sum driver contributions into headline buckets (Dollar bloc, Rates, ...)."""
    groups: dict[str, list[str]] = {}
    meta = {**SERIES, **ECOS_SERIES}
    for col in att.columns:
        if col in meta and col != TARGET:
            groups.setdefault(meta[col][-1], []).append(col)
    g = pd.DataFrame({name: att[cols].sum(axis=1) for name, cols in groups.items()})
    g["Unexplained (KRW-specific)"] = att["residual"]
    return g


@dataclass
class Evaluation:
    oos_r2: float          # 1 - SSE / sum(y^2), betas from t-1 only
    hit_rate: float        # share of days the fitted move has the right sign
    in_sample_r2: float    # full-sample OLS R^2 (optimistic by construction)
    n_days: int


def evaluate(att: pd.DataFrame, full_r2: float) -> Evaluation:
    y, f = att["actual"], att["fitted"]
    e = y - f
    oos = 1.0 - (e**2).sum() / (y**2).sum()  # zero-move benchmark: no look-ahead
    hits = (np.sign(f) == np.sign(y))[y != 0].mean()
    return Evaluation(float(oos), float(hits), float(full_r2), int(len(att)))


def full_sample_hac(y: pd.Series, X: pd.DataFrame, lags: int = HAC_LAGS):
    """Full-sample OLS with Newey-West (HAC) standard errors."""
    res = sm.OLS(y, sm.add_constant(X)).fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    table = pd.DataFrame({"beta": res.params, "t_stat": res.tvalues, "p_value": res.pvalues})
    return table, float(res.rsquared)


def key_levels(level: pd.Series) -> dict[str, float]:
    """Desk-style key levels for the target series."""
    last = float(level.iloc[-1])
    rets = np.log(level).diff().dropna()
    return {
        "last": last,
        "chg_1d_pct": float(rets.iloc[-1] * 100),
        "ma20": float(level.tail(20).mean()),
        "ma60": float(level.tail(60).mean()),
        "high_1m": float(level.tail(21).max()),
        "low_1m": float(level.tail(21).min()),
        "high_3m": float(level.tail(63).max()),
        "low_3m": float(level.tail(63).min()),
        "rvol_20d_ann_pct": float(rets.tail(20).std() * np.sqrt(252) * 100),
        "move_z": float(rets.iloc[-1] / rets.tail(60).std()) if len(rets) > 60 else float("nan"),
    }
