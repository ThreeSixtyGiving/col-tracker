import pandas as pd
from dash import dcc

from ..settings import AMOUNT_BIN_LABELS, AMOUNT_BINS, THREESIXTY_COLOURS
from ._utils import card_wrapper, horizontal_bar


def awardamount(grants):
    amount_bins = pd.cut(
        grants["amountAwarded"],
        bins=AMOUNT_BINS,
        labels=AMOUNT_BIN_LABELS,
    )
    amounts = [
        {"name": i, "count": count}
        for i, count in amount_bins.value_counts().sort_index().items()
    ]
    count_unknown = amount_bins.isnull().sum()
    if count_unknown:
        amounts.append({"name": "Unknown", "count": count_unknown})

    return card_wrapper(
        "Grant amount",
        [
            dcc.Graph(
                id="amount-chart-chart",
                figure=horizontal_bar(
                    amounts,
                    colour=THREESIXTY_COLOURS[0],
                ),
                config={"displayModeBar": False, "scrollZoom": False},
            ),
        ],
        subtitle="Number of grants",
        colour="orange",
    )
