"""Data loading: Yahoo Finance, FRED, optional ECOS (Bank of Korea) and KRX flows.

Every fetch returns a price/level series indexed by date. Levels are aligned on
common trading dates BEFORE returns are computed, so each daily change covers the
same calendar interval for every series (no holiday-filled 0% days).
"""

from __future__ import annotations

import io
import json
import os
import urllib.request
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

from .config import ECOS_SERIES, FALLBACKS, MIN_COVERAGE, MIN_HISTORY, NY_CLOSE, SERIES, TARGET


# ---------------------------------------------------------------- fetchers
def fetch_yahoo(ticker: str, start: str, attempts: int = 3) -> pd.Series:
    """Daily closes from Yahoo, trying two yfinance methods with retries."""
    import time

    import yfinance as yf

    last_err: Exception | None = None
    for i in range(attempts):
        try:
            df = yf.Ticker(ticker).history(start=start, auto_adjust=True)
            if df is None or df.empty:
                df = yf.download(ticker, start=start, auto_adjust=True, progress=False)
            if df is not None and not df.empty:
                close = df["Close"]
                if isinstance(close, pd.DataFrame):  # newer yfinance: MultiIndex columns
                    close = close.iloc[:, 0]
                idx = pd.to_datetime(close.index)
                if idx.tz is not None:
                    idx = idx.tz_localize(None)
                close.index = idx.normalize()
                return close.astype(float).dropna()
        except Exception as exc:  # network / Yahoo format changes
            last_err = exc
        time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Yahoo returned no data for {ticker} ({last_err})")


def fetch_krx_index(code: str, start: str) -> pd.Series:
    """KRX index closes via pykrx (code '1001' = KOSPI). Optional dependency."""
    from pykrx import stock

    begin = pd.Timestamp(start).strftime("%Y%m%d")
    end = pd.Timestamp.today().strftime("%Y%m%d")
    df = stock.get_index_ohlcv(begin, end, code)
    close = df[[c for c in df.columns if "종가" in str(c) or str(c).lower() == "close"][0]]
    close.index = pd.to_datetime(close.index)
    return close.astype(float).dropna()


def _ssl_context():
    """SSL context using certifi's CA bundle (python.org builds on macOS ship without one)."""
    import ssl

    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def _get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "krw-driver-monitor"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
        return r.read()


def fetch_fred(code: str, start: str) -> pd.Series:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={code}&cosd={start}"
    df = pd.read_csv(io.BytesIO(_get(url)))
    s = pd.to_numeric(df[code], errors="coerce")  # FRED marks missing days with "."
    s.index = pd.to_datetime(df[df.columns[0]])
    return s.dropna()


def fetch_ecos(stat_code: str, item_code: str, start: str, api_key: str) -> pd.Series:
    begin = pd.Timestamp(start).strftime("%Y%m%d")
    end = pd.Timestamp.today().strftime("%Y%m%d")
    url = (
        f"https://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/100000/"
        f"{stat_code}/D/{begin}/{end}/{item_code}"
    )
    payload = json.loads(_get(url))
    rows = payload.get("StatisticSearch", {}).get("row", [])
    if not rows:
        raise RuntimeError(f"ECOS returned no rows for {stat_code}/{item_code}: {payload}")
    s = pd.Series(
        [float(r["DATA_VALUE"]) for r in rows],
        index=pd.to_datetime([r["TIME"] for r in rows], format="%Y%m%d"),
    )
    return s.sort_index()


def fetch_foreign_flows(start: str) -> pd.Series | None:
    """KOSPI foreign investors' net buying, KRW 100m (억원). Optional: needs pykrx."""
    try:
        from pykrx import stock
    except ImportError:
        return None
    begin = pd.Timestamp(start).strftime("%Y%m%d")
    end = pd.Timestamp.today().strftime("%Y%m%d")
    try:
        df = stock.get_market_trading_value_by_date(begin, end, "KOSPI")
    except Exception as exc:  # KRX endpoints change; never let flows break the run
        warnings.warn(f"Foreign flows unavailable: {exc}")
        return None
    cols = [c for c in df.columns if "외국인" in str(c)]
    if not cols:
        return None
    s = df[cols[0]].astype(float) / 1e8
    s.index = pd.to_datetime(s.index)
    return s.rename("KOSPI_FOREIGN_NET")


def _fetch(source: str, code: str, start: str) -> pd.Series:
    if source == "yahoo":
        return fetch_yahoo(code, start)
    if source == "fred":
        return fetch_fred(code, start)
    if source == "krx":
        return fetch_krx_index(code, start)
    raise ValueError(f"unknown source {source}")


# ---------------------------------------------------------------- loading
def load_levels(start: str, cache_dir: Path, offline: bool = False) -> pd.DataFrame:
    """Return a DataFrame of raw levels, one column per series (not yet aligned)."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache = cache_dir / "levels.csv"
    if offline:
        if not cache.exists():
            raise FileNotFoundError(f"--offline given but no cache at {cache}")
        return pd.read_csv(cache, index_col=0, parse_dates=True)

    cols: dict[str, pd.Series] = {}
    for name, (source, code, label, *_rest) in SERIES.items():
        attempts = [(source, code, label)] + FALLBACKS.get(name, [])
        errors = []
        for i, (src, cd, desc) in enumerate(attempts):
            try:
                s = _fetch(src, cd, start)
                if len(s) < MIN_HISTORY:
                    raise RuntimeError(f"only {len(s)} rows returned")
                cols[name] = s
                if i > 0:
                    warnings.warn(f"{name}: using fallback {desc} ({'; '.join(errors)})")
                break
            except Exception as exc:
                errors.append(f"{src}:{cd} failed: {exc}")
        else:
            if name == TARGET:
                raise RuntimeError(f"Could not load {name} from any source: {errors}")
            warnings.warn(f"Skipping {name}: {'; '.join(errors)}")

    key = os.environ.get("ECOS_API_KEY")
    if key:
        for name, (stat, item, *_rest) in ECOS_SERIES.items():
            try:
                cols[name] = fetch_ecos(stat, item, start, key)
            except Exception as exc:
                warnings.warn(f"Skipping {name} (ECOS): {exc}")

    levels = pd.DataFrame(cols).sort_index()
    levels.to_csv(cache)
    return levels


def to_changes(levels: pd.DataFrame) -> pd.DataFrame:
    """Align on common dates, then convert levels to daily changes.

    Prices -> log returns in %; yields -> changes in basis points.
    Drivers in NY_CLOSE are lagged one day to match USD/KRW's session timing.
    """
    transforms = {n: t for n, (_s, _c, t, *_r) in SERIES.items()}
    transforms.update({n: t for n, (_s, _c, t, *_r) in ECOS_SERIES.items()})

    # Drop drivers too sparse to align with USD/KRW, rather than losing every date.
    base = levels[TARGET].notna()
    keep = [TARGET]
    for col in levels.columns:
        if col == TARGET:
            continue
        coverage = levels.loc[base, col].notna().mean()
        if coverage >= MIN_COVERAGE:
            keep.append(col)
        else:
            warnings.warn(f"Dropping {col}: data on only {coverage:.0%} of USD/KRW dates")
    aligned = levels[keep].dropna(how="any")  # common trading dates only
    out = {}
    for col in aligned.columns:
        x = aligned[col]
        if transforms.get(col) == "diff_bp":
            out[col] = x.diff() * 100.0  # yields are quoted in %, so ×100 = bp
        else:
            out[col] = np.log(x).diff() * 100.0
    changes = pd.DataFrame(out)
    # New York-close drivers: yesterday's NY move explains today's Seoul-session move.
    for col in changes.columns:
        if col in NY_CLOSE:
            changes[col] = changes[col].shift(1)
    return changes.dropna()
