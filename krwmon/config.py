"""Series definitions and defaults for the USD/KRW driver monitor."""

from __future__ import annotations

# name -> (source, code, transform, label, group)
#   source:    "yahoo" | "fred"
#   transform: "logret" -> daily log return in %; "diff_bp" -> daily change in basis points
#   group:     bucket used in the daily headline attribution
TARGET = "USDKRW"

SERIES: dict[str, tuple[str, str, str, str, str]] = {
    "USDKRW": ("yahoo", "KRW=X", "logret", "USD/KRW spot (KRW per USD)", "target"),
    "DXY": ("yahoo", "DX-Y.NYB", "logret", "US Dollar Index", "Dollar bloc"),
    "USDCNH": ("yahoo", "CNH=X", "logret", "USD/CNH (offshore yuan)", "Dollar bloc"),
    "KOSPI": ("yahoo", "^KS11", "logret", "KOSPI index", "Korean equities"),
    "UST2Y": ("fred", "DGS2", "diff_bp", "US 2y Treasury yield", "Rates"),
    "BRENT": ("yahoo", "BZ=F", "logret", "Brent crude (front month)", "Oil"),
}

# Optional driver: Korea 3y government bond yield from the Bank of Korea ECOS API.
# Requires a free API key in the ECOS_API_KEY environment variable.
# Stat/item codes: 817Y002 = market interest rates (daily), 010200000 = KTB 3y.
# Verify the codes on ecos.bok.or.kr if the request returns no rows.
ECOS_SERIES = {
    "KTB3Y": ("817Y002", "010200000", "diff_bp", "Korea 3y KTB yield (ECOS)", "Rates"),
}

DEFAULT_START = "2018-01-01"
DEFAULT_WINDOW = 120  # trading days in each rolling regression (~6 months)
HAC_LAGS = 5

# Chart palette (validated for colour-vision deficiency; see README)
PALETTE = {
    "DXY": "#2a78d6",
    "USDCNH": "#eb6834",
    "KOSPI": "#1baf7a",
    "UST2Y": "#eda100",
    "BRENT": "#e87ba4",
    "KTB3Y": "#4a3aa7",
    "residual": "#9a9893",
}
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e6e4df"
SURFACE = "#fcfcfb"
