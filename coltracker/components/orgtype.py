from dash import dcc

from ..settings import THREESIXTY_COLOURS
from ._utils import horizontal_bar, card_wrapper


def orgtype(grants):
    orgtypes = [
        {"name": i.replace("-", " ").title(), "count": count}
        for i, count in grants["_recipient_type"].value_counts().items()
    ]
    count_unknown = grants["_recipient_type"].isnull().sum()
    if count_unknown:
        orgtypes.append({"name": "Unknown", "count": count_unknown})

    return card_wrapper(
        "Type of recipients",
        [
            dcc.Graph(
                id="orgtype-chart-chart",
                figure=horizontal_bar(
                    orgtypes,
                    colour=THREESIXTY_COLOURS[3],
                ),
                config={"displayModeBar": False, "scrollZoom": False},
            ),
        ],
        subtitle="Number of grants",
        colour="red",
    )
