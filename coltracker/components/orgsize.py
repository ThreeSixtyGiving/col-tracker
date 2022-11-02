import pandas as pd
from dash import dcc

from ..settings import INCOME_BIN_LABELS, INCOME_BINS, THREESIXTY_COLOURS
from ._utils import card_wrapper, horizontal_bar


def orgsize(grants):
    orgsize_bins = pd.cut(
        grants["_recipient_income"],
        bins=INCOME_BINS,
        labels=INCOME_BIN_LABELS,
    )
    orgsizes = [
        {"name": i, "count": count}
        for i, count in orgsize_bins.value_counts().sort_index().items()
    ]
    count_unknown = orgsize_bins.isnull().sum()
    if count_unknown:
        orgsizes.append({"name": "Unknown / Not a charity", "count": count_unknown})

    return card_wrapper(
        "Income of recipients",
        [
            dcc.Graph(
                id="orgsize-chart-chart",
                figure=horizontal_bar(
                    orgsizes,
                    colour=THREESIXTY_COLOURS[0],
                ),
                config={"displayModeBar": False, "scrollZoom": False},
            ),
        ],
        subtitle="Number of grants (Registered charities only)",
        colour="orange",
    )
