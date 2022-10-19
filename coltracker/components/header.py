from dash import html


def header():
    return html.Header(
        className="layout__header",
        children=[
            html.Div(
                className="nav-bar",
                children=[
                    html.A(
                        className="nav-bar__home-button",
                        href="/",
                        children=[
                            html.Img(
                                src="https://www.threesixtygiving.org/wp-content/themes/360giving2020/assets/images/360-logos/360giving-main.svg",
                                alt="360 Main",
                            ),
                            html.Span(className="screen-reader-only", children="Home"),
                        ],
                    ),
                    html.H1(
                        className="nav-bar__title",
                        children=[
                            html.A(
                                className="",
                                href="/",
                                children="Cost of Living Grants Tracker",
                            )
                        ],
                    ),
                    html.Nav(
                        className="nav-bar__nav-menu",
                        children=[
                            html.Ul(
                                children=[
                                    html.Li(
                                        className="nav-menu-item",
                                        children=[
                                            html.A(
                                                className="nav-menu__button",
                                                href="https://threesixtygiving.org/",
                                                children="About 360Giving",
                                            )
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
