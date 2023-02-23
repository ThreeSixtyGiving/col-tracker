from dash import dcc, html

from .chart import chart


def tab_dashboard(data, all_data):
    return dcc.Tab(
        label="Dashboard",
        value="dashboard",
        className="",
        selected_className="",
        children=[
            html.Div(
                className="grid grid--two-columns",
                children=[
                    html.Div(
                        id="data-chart",
                        className="grid__all",
                        children=[
                            chart(data["grants"]),
                        ],
                    ),
                    html.Div(
                        className="grid__1",
                        children=[
                            dcc.Markdown(
                                """
        This tracker is possible thanks to UK grantmakers publishing grants data using the [360Giving Data Standard](http://standard.threesixtygiving.org/en/latest/). It only includes grants awarded in British Pounds (GBP) that have already been made (rather than amounts committed to grant programmes).

        Grants are included if they use the terms "cost of living" somewhere in the grant description, title, or grant programme description or title. This is based on the [guidance for grantmakers](https://www.threesixtygiving.org/2022/09/28/col/) issued by 360Giving on tagging grants.
        
        This tracker does not present the totality of funding provided in response to the crisis. In some cases, only a small proportion of the total grant amount recorded is in response to the cost of living crisis. Also, some funders have chosen to not tag grants with “cost of living” where they feel that all their grants support people in financial hardship, so these grants will not appear in the tracker.
    """
                            )
                        ],
                    ),
                    html.Div(
                        className="grid__1",
                        children=[
                            dcc.Markdown(
                                """
        Not all grantmakers publish their grants as open data, and some publishers do not immediately publish their latest data.

        Some of the data includes grants made to other grantmakers to distribute. These are highlighted in the dashboard above.You can choose to exclude these grants from the data to prevent skews to analysis this might cause.
    """
                            ),
                            dcc.Markdown(
                                """
        For more information please contact [labs@threesixtygiving.org](mailto:labs@threesixtygiving.org).
    """
                            ),
                        ],
                    ),
                    html.Div(
                        id="top-funders",
                        className="",
                        children=[],
                    ),
                    html.Div(
                        id="award-amount",
                        className="",
                        children=[],
                    ),
                    html.Div(
                        id="regions-chart",
                        className="",
                        children=[],
                    ),
                    html.Div(
                        id="organisation-type",
                        className="",
                        children=[],
                    ),
                    html.Div(
                        id="organisation-size",
                        className="",
                        children=[],
                    ),
                    html.Div(
                        id="word-cloud",
                        className="grid__all",
                        children=[],
                    ),
                ],
            ),
        ],
    )
