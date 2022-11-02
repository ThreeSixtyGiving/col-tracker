from dash import dcc
from dash import html

from ..settings import THREESIXTY_COLOURS
from ._utils import horizontal_bar, card_wrapper
from .geomap import sources


def region_wrapper(content: list, subtitle: str = None, region_type: str = "region"):
    return html.Div(
        className="base-card base-card--teal grid__1",
        children=[
            html.Div(
                className="base-card__content",
                children=[
                    html.Header(
                        className="base-card__header",
                        children=[
                            html.H3(
                                className="base-card__heading",
                                children="Grants by {}".format(region_type),
                            ),
                            html.H4(
                                className="base-card__subheading", children=subtitle
                            )
                            if subtitle
                            else None,
                        ],
                    )
                ]
                + content,
            ),
        ],
    )


def regions(grants):
    area_types = [
        ("location.ladcd", "location.ladnm", "Local Authority District"),
        ("location.utlacd", "location.utlanm", "Local Authority"),
        ("location.rgnctrycd", "location.rgnctrynm", "Country and Region"),
        ("location.rgncd", "location.rgnnm", "Region"),
    ]
    for a in area_types:
        if a[0] not in grants.columns:
            continue
        regions = grants[grants[a[0]] != ""].groupby([a[0], a[1]]).size()
        region_type = a[2]
        if len(regions) > 1 and len(regions) < 100:
            break

    if len(regions) <= 1:
        return card_wrapper("Grants by Region", [html.P("No data available")])

    regions = [{"name": i[1], "count": count} for i, count in regions.items()]
    subtitle = None
    if region_type.startswith("Local Authority"):
        regions = sorted(regions, key=lambda x: -x["count"])
        if len(regions) > 12:
            regions = regions[:12]
            subtitle = "Top {:,.0f} local authorities".format(12)

    return card_wrapper(
        "Grants by {}".format(region_type),
        [
            dcc.Graph(
                id="regions-chart-chart",
                figure=horizontal_bar(
                    regions,
                    colour=THREESIXTY_COLOURS[1],
                ),
                config={"displayModeBar": False, "scrollZoom": False},
            ),
            sources(grants["location.source"]),
        ],
        subtitle=subtitle,
        colour="teal",
    )
