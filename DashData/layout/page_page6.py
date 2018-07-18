# enconding: utf-8

import dash_html_components as html
from DashData.components.layout import page_contents


def page_page6_row1():
    return html.Div([
        html.Div([
            html.H6('Vanguard News',
                    className="gs-header gs-text-header padded"),
            html.Br([]),
            html.P('10/25/16    The rise of indexing and the fall of costs'),
            html.Br([]),
            html.P(
                "08/31/16    It's the index mutual fund's 40th anniversary: \
                Let the low-cost, passive party begin")
        ], className="six columns"),

        html.Div([
            html.H6("Reviews",
                    className="gs-header gs-table-header padded"),
            html.Br([]),
            html.Li('Launched in 1976.'),
            html.Li(
                'On average, has historically produced returns that have far \
                outpaced the rate of inflation.*'),
            html.Li(
                "Vanguard Quantitative Equity Group, the fund's advisor, is \
                among the world's largest equity index managers."),
            html.Br([]),
            html.P("Did you know? The fund launched in 1976 as Vanguard First \
            Index Investment Trust—the nation's first index fund available to \
            individual investors."),
            html.Br([]),
            html.P(
                "* The performance of an index is not an exact representation \
                of any particular investment, as you cannot invest directly \
                in an index."),
            html.Br([]),
            html.P(
                "Past performance is no guarantee of future returns. See \
                performance data current to the most recent month-end.")
        ], className="six columns"),

    ], className="row ")


def page_page6_content():
    return page_contents([
        page_page6_row1()
    ])
    # return html.Div([  # page 6
    #     print_button(),
    #     html.Div([
    #         page_header(),
    #         page_page6_row1()
    #     ], className="subpage")

    # ], className="page")
