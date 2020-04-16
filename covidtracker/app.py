import json
import os

import dash
import dash_core_components as dcc
import dash_html_components as html

from data import get_data
from components import cards, chart, table

app = dash.Dash(__name__)

with open(os.path.join(os.path.dirname(__file__), 'templates/dash.html'), encoding='utf8') as a:
    app.index_string = a.read()

data = get_data()

app.layout = html.Div(children=[

    cards(data),
    html.Div(className="spacer-3"),
    html.Div(className="grid grid--two-columns", children=[
        html.Div(className="grid__all", children=[
            chart(data),
        ]),
    ]),
    html.Div(className="spacer-3"),
    html.Div(className="grid grid--two-columns", children=[
        html.Div(className="grid__1", children=[
            dcc.Markdown('''
                This data is based on UK foundations reporting grants using the
                360Giving Data Standard. It only includes grants that have already
                been made (rather than amounts committed to grant programmes).
            ''')
        ]),
        html.Div(className="grid__1", children=[
            dcc.Markdown('''
                Not all foundations publish their grants as open data, and some
                publishers do not immediately publish their latest data. 

                For more information please contact [labs@threesixtygiving.org](mailto:labs@threesixtygiving.org).
            '''),
        ]),
    ]),
    html.Div(className="grid grid--two-columns", children=[
        html.Div(className="grid__all", children=[
            table(data),
        ]),
        html.Div(className="grid__all", children=[
            dcc.Markdown('''
                [GrantNav](https://grantnav.threesixtygiving.org/) is search-engine
                for grants data. Explore and download in detail on where and how much funding 
                goes across billions of pounds of grants.
            '''),
            html.A(className='button button--orange', href="data/grants_data.json", target="_blank", children="Download (JSON)"),
            ' ',
            html.A(className='button button--orange', href="https://grantnav.threesixtygiving.org/search?json_query=%7B%22query%22%3A+%7B%22bool%22%3A+%7B%22must%22%3A+%7B%22query_string%22%3A+%7B%22query%22%3A+%22coronavirus+OR+pandemic+OR+covid+OR+%5C%22covid19%5C%22%22%2C+%22default_field%22%3A+%22%2A%22%7D%7D%2C+%22filter%22%3A+%5B%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%2C+%22must%22%3A+%7B%7D%2C+%22minimum_should_match%22%3A+1%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%7B%22range%22%3A+%7B%22amountAwarded%22%3A+%7B%7D%7D%7D%2C+%22must%22%3A+%7B%7D%2C+%22minimum_should_match%22%3A+1%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%7B%22range%22%3A+%7B%22awardDate%22%3A+%7B%22format%22%3A+%22year%22%2C+%22gte%22%3A+%222020%7C%7C%2Fy%22%2C+%22lte%22%3A+%222020%7C%7C%2Fy%22%7D%7D%7D%5D%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%7D%7D%2C+%7B%22bool%22%3A+%7B%22should%22%3A+%5B%5D%7D%7D%5D%7D%7D%2C+%22sort%22%3A+%7B%22_score%22%3A+%7B%22order%22%3A+%22desc%22%7D%7D%2C+%22aggs%22%3A+%7B%22fundingOrganization%22%3A+%7B%22terms%22%3A+%7B%22field%22%3A+%22fundingOrganization.id_and_name%22%2C+%22size%22%3A+50%7D%7D%2C+%22recipientOrganization%22%3A+%7B%22terms%22%3A+%7B%22field%22%3A+%22recipientOrganization.id_and_name%22%2C+%22size%22%3A+3%7D%7D%2C+%22recipientRegionName%22%3A+%7B%22terms%22%3A+%7B%22field%22%3A+%22recipientRegionName%22%2C+%22size%22%3A+3%7D%7D%2C+%22recipientDistrictName%22%3A+%7B%22terms%22%3A+%7B%22field%22%3A+%22recipientDistrictName%22%2C+%22size%22%3A+3%7D%7D%2C+%22currency%22%3A+%7B%22terms%22%3A+%7B%22field%22%3A+%22currency%22%2C+%22size%22%3A+3%7D%7D%7D%2C+%22extra_context%22%3A+%7B%22awardYear_facet_size%22%3A+3%2C+%22amountAwardedFixed_facet_size%22%3A+3%7D%7D", target="_blank", children="Search on GrantNav"),
            html.Div(className="spacer-3"),
            html.P(
                html.Small(
                    html.Em([
                        'Last updated ',
                        "{:%Y-%m-%d %H:%M}".format(data["last_updated"]),
                    ]),
                ),
            ),
        ]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
