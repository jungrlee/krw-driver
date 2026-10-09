"""Charts and the daily desk note (Markdown)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

from .config import ECOS_SERIES, GRID, INK, INK_SECONDARY, PALETTE, SERIES, SURFACE  # noqa: E402

LABELS = {n: v[3] for n, v in {**SERIES, **ECOS_SERIES}.items()}
UNITS = {n: ("% per 1bp" if v[2] == "diff_bp" else "% per 1%") for n, v in {**SERIES, **ECOS_SERIES}.items()}


def _style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK_SECONDARY, labelsize=8)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def chart_price(level: pd.Series, path: Path) -> None:
    s = level.tail(252)
    fig, ax = plt.subplots(figsize=(8, 3.2), facecolor=SURFACE)
    _style(ax)
    ax.plot(s.index, s, color=PALETTE["DXY"], linewidth=2, label="USD/KRW")
    ax.plot(s.index, s.rolling(20).mean(), color=INK_SECONDARY, linewidth=1, linestyle="--", label="20d MA")
    ax.plot(s.index, s.rolling(60).mean(), color=INK_SECONDARY, linewidth=1, linestyle=":", label="60d MA")
    ax.set_title("USD/KRW, last 12 months (KRW per USD)", loc="left", fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK_SECONDARY, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def chart_betas(betas: pd.DataFrame, path: Path) -> None:
    cols = [c for c in betas.columns if c != "const"]
    b = betas[cols].dropna()
    fig, axes = plt.subplots(len(cols), 1, figsize=(8, 1.5 * len(cols)), sharex=True, facecolor=SURFACE)
    axes = [axes] if len(cols) == 1 else axes
    for ax, c in zip(axes, cols):
        _style(ax)
        ax.axhline(0, color=INK_SECONDARY, linewidth=0.8)
        ax.plot(b.index, b[c], color=PALETTE.get(c, INK), linewidth=1.6)
        ax.set_title(f"{LABELS.get(c, c)}  ({UNITS.get(c, '')})", loc="left", fontsize=9, color=INK)
    fig.suptitle("Rolling sensitivity of USD/KRW to each driver", x=0.01, ha="left", fontsize=10, color=INK)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def chart_attribution(att: pd.DataFrame, path: Path, days: int = 20) -> None:
    drivers = [c for c in att.columns if c not in ("residual", "fitted", "actual")]
    a = att.tail(days)
    cols = drivers + ["residual"]
    x = range(len(a))
    fig, ax = plt.subplots(figsize=(8, 3.6), facecolor=SURFACE)
    _style(ax)
    pos_base = pd.Series(0.0, index=a.index)
    neg_base = pd.Series(0.0, index=a.index)
    for c in cols:
        v = a[c]
        pos, neg = v.clip(lower=0), v.clip(upper=0)
        color = PALETTE.get(c, INK_SECONDARY)
        label = "Unexplained" if c == "residual" else c
        ax.bar(x, pos, bottom=pos_base, color=color, width=0.72, edgecolor=SURFACE, linewidth=1, label=label)
        ax.bar(x, neg, bottom=neg_base, color=color, width=0.72, edgecolor=SURFACE, linewidth=1)
        pos_base += pos
        neg_base += neg
    ax.scatter(x, a["actual"], color=INK, s=18, zorder=5, label="Actual move")
    ax.axhline(0, color=INK_SECONDARY, linewidth=0.8)
    ax.set_xticks(list(x))
    ax.set_xticklabels([d.strftime("%m-%d") for d in a.index], rotation=90, fontsize=7)
    ax.set_ylabel("% change in USD/KRW", fontsize=8, color=INK_SECONDARY)
    ax.set_title(f"What moved USD/KRW: last {days} trading days", loc="left", fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=7, ncol=4, labelcolor=INK_SECONDARY, loc="upper left", bbox_to_anchor=(0, -0.28))
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def _fmt_pp(x: float) -> str:
    return f"{x:+.2f}pp"


def headline(levels: dict, groups_last: pd.Series, date: pd.Timestamp) -> str:
    move = levels["chg_1d_pct"]
    verb = "rose" if move > 0 else "fell" if move < 0 else "was unchanged"
    parts = [f"{name} {_fmt_pp(v)}" for name, v in groups_last.drop("Unexplained (KRW-specific)").items()]
    biggest = groups_last.abs().idxmax()
    resid = groups_last["Unexplained (KRW-specific)"]
    return (
        f"USD/KRW {verb} {abs(move):.2f}% to {levels['last']:,.1f} on {date:%d %b %Y}. "
        f"The driver model attributes {', '.join(parts)}; {_fmt_pp(resid)} is unexplained "
        f"(KRW-specific flows or positioning). Largest single bucket: **{biggest}**."
    )


def write_note(
    out_dir: Path,
    levels: dict,
    att: pd.DataFrame,
    groups: pd.DataFrame,
    hac_table: pd.DataFrame,
    ev,
    window: int,
    betas_now: pd.Series,
    flows: pd.Series | None = None,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    img = out_dir / "img"
    img.mkdir(exist_ok=True)
    date = att.index[-1]

    last20 = groups.tail(20).sum()
    lines = [
        f"# USD/KRW Driver Note — {date:%Y-%m-%d}",
        "",
        headline(levels, groups.iloc[-1], date),
        "",
        "## Key levels",
        "",
        "| Level | Value |",
        "|---|---|",
        f"| Last | {levels['last']:,.1f} |",
        f"| 1-day change | {levels['chg_1d_pct']:+.2f}% (z = {levels['move_z']:+.1f} vs 60d vol) |",
        f"| 20d / 60d moving average | {levels['ma20']:,.1f} / {levels['ma60']:,.1f} |",
        f"| 1-month range | {levels['low_1m']:,.1f} – {levels['high_1m']:,.1f} |",
        f"| 3-month range | {levels['low_3m']:,.1f} – {levels['high_3m']:,.1f} |",
        f"| 20d realised vol (annualised) | {levels['rvol_20d_ann_pct']:.1f}% |",
        "",
        f"![USD/KRW](img/{date:%Y-%m-%d}_price.png)",
        "",
        "## Attribution",
        "",
        "| Bucket | Last day | Last 20 days (cumulative) |",
        "|---|---|---|",
    ]
    for name in groups.columns:
        lines.append(f"| {name} | {_fmt_pp(groups[name].iloc[-1])} | {_fmt_pp(last20[name])} |")
    lines += [
        f"| **Actual USD/KRW move** | **{att['actual'].iloc[-1]:+.2f}%** | **{att['actual'].tail(20).sum():+.2f}%** |",
        "",
        f"![Attribution](img/{date:%Y-%m-%d}_attribution.png)",
        "",
        "## Current sensitivities",
        "",
        f"Rolling {window}-day betas (point in time). Full-sample betas use Newey-West (HAC) t-stats.",
        "",
        "| Driver | Rolling beta (now) | Full-sample beta | t-stat |",
        "|---|---|---|---|",
    ]
    for drv in [i for i in hac_table.index if i != "const"]:
        now = float(betas_now.get(drv, float("nan")))
        lines.append(
            f"| {LABELS.get(drv, drv)} ({UNITS.get(drv, '')}) | {now:+.3f} | "
            f"{hac_table.loc[drv, 'beta']:+.3f} | {hac_table.loc[drv, 't_stat']:+.1f} |"
        )
    lines += ["", f"![Rolling betas](img/{date:%Y-%m-%d}_betas.png)", ""]

    if flows is not None and len(flows):
        f5 = flows.tail(5)
        lines += [
            "## Foreign equity flows (KOSPI, KRW 100m)",
            "",
            "| Date | Foreign net buy |",
            "|---|---|",
            *[f"| {d:%Y-%m-%d} | {v:+,.0f} |" for d, v in f5.items()],
            f"| **5-day total** | **{f5.sum():+,.0f}** |",
            "",
        ]

    lines += [
        "## How reliable is this?",
        "",
        f"- Out-of-sample explained share of daily moves: **{ev.oos_r2:.0%}** "
        f"(betas estimated through the previous day only; {ev.n_days:,} days).",
        f"- In-sample R² for comparison: {ev.in_sample_r2:.0%} — optimistic by construction.",
        f"- Sign of the move matched on **{ev.hit_rate:.0%}** of days.",
        "- This is attribution, not a forecast: same-day drivers explain same-day moves.",
        "- Timing: USD/KRW is matched with the previous New York session for DXY, US yields and oil, "
        "and with the same Seoul session for KOSPI. Close times still differ, so read 20-day totals "
        "with more confidence than single days.",
        "",
    ]
    path = out_dir / f"{date:%Y-%m-%d}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    (out_dir / "latest.md").write_text("\n".join(lines), encoding="utf-8")
    return path
