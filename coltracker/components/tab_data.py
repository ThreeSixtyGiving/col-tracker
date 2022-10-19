from dash import dcc
from dash import html

from .datasources import datasources
from .table import table


def tab_data(data, all_data):
    return dcc.Tab(
        label="Data",
        value="data",
        className="",
        selected_className="",
        children=[
            html.Div(
                className="grid grid--two-columns",
                children=[
                    html.Div(
                        className="grid__all",
                        children=[
                            html.Div(
                                [
                                    html.H3(
                                        className="h3",
                                        children="Grants",
                                    ),
                                    html.Div(
                                        className="table table--zebra",
                                        id="data-table",
                                        children=[table(data["grants"])],
                                    ),
                                ]
                            )
                        ],
                    ),
                    html.Div(
                        className="grid__all",
                        children=[
                            dcc.Markdown(
                                """
        [GrantNav](https://grantnav.threesixtygiving.org/) is search-engine
        for grants data. Explore and download in detail on where and how much funding
        goes across billions of pounds of grants.
    """
                            ),
                            html.A(
                                className="button button--orange",
                                href="/data/grants.csv",
                                target="_blank",
                                children="Download all grants (CSV)",
                            ),
                            " ",
                            html.A(
                                className="button button--orange",
                                href="/data/grants.json",
                                target="_blank",
                                children="Download all grants (JSON)",
                            ),
                            " ",
                            html.A(
                                className="button button--orange",
                                href="/data/la.csv",
                                target="_blank",
                                children="Download Local Authority summaries (CSV)",
                            ),
                            " ",
                            html.A(
                                className="button button--orange",
                                href="https://grantnav.threesixtygiving.org/search?query=%22cost+of+living%22&default_field=*&sort=_score+desc",
                                target="_blank",
                                children="Search on GrantNav",
                            ),
                            html.Div(className="spacer-3"),
                            html.P(
                                html.Small(
                                    html.Em(
                                        id="last-updated",
                                        children=[
                                            "Last updated ",
                                            "{:%Y-%m-%d %H:%M}".format(
                                                data["last_updated"]
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                            html.H3(
                                className="h3",
                                children="Data Sources",
                            ),
                            html.Div(
                                className="table table--zebra",
                                id="data-sources",
                                children=[datasources(data["grants"])],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
