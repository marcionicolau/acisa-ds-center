# enconding: utf-8

import dash_html_components as html
from DashData.components.layout import (page_contents,
                                        make_dash_table)

from DashData.datasets.all_data import (
    df_dividend, df_realized, df_unrealized)


def page_page5_row1():
    return html.Div([
        html.Div([
            html.H6(["Distributions"],
                    className="gs-header gs-table-header padded"),
            html.Strong(
                ["Distributions for this fund are scheduled quaterly"])
        ], className="twelve columns"),
    ], className="row ")


def page_page5_row2():
    return html.Div([
        html.Div([
            html.Br([]),
            html.H6(["Dividend and capital gains distributions"],
                    className="gs-header gs-table-header tiny-header"),
            html.Table(make_dash_table(df_dividend),
                       className="tiny-header")
        ], className="twelve columns"),
    ], className="row ")


def page_page5_row3():
    return html.Div([
        html.Div([
            html.H6(["Realized/unrealized gains as of 01/31/2018"],
                    className="gs-header gs-table-header tiny-header")
        ], className=" twelve columns")
    ], className="row ")


def page_page5_row4():
    return html.Div([
        html.Div([
            html.Table(make_dash_table(df_realized))
        ], className="six columns"),
        html.Div([
            html.Table(make_dash_table(df_unrealized))
        ], className="six columns"),
    ], className="row "),


def page_page5_content():
    return page_contents(
        page_page5_row1(),
        page_page5_row2(),
        page_page5_row3(),
        page_page5_row4()
    )
