# encoding: utf-8

import dash_html_components as html
import dash_core_components as dcc
from DashData.components.layout import (page_contents,
                                        make_dash_table)
from DashData.datasets.all_data import (df_current_prices, df_hist_prices,
                                        df_graph, df_avg_returns, df_after_tax,
                                        df_recent_returns)

import plotly.graph_objs as go


def page_page2_row1():
    return html.Div([
        html.Div([
            html.H6(["Current Prices"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(df_current_prices))

        ], className="six columns"),

        html.Div([
            html.H6(["Historical Prices"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(df_hist_prices))
        ], className="six columns"),

    ], className="row ")


def page_page2_row2():
    return html.Div([
        html.Div([
            html.H6("Performance",
                    className="gs-header gs-table-header padded"),
            dcc.Graph(
                id='graph-4',
                figure={
                    'data': [
                        go.Scatter(
                            x=df_graph['Date'],
                            y=df_graph['Vanguard 500 Index Fund'],
                            line={"color": "rgb(53, 83, 255)"},
                            mode="lines",
                            name="Vanguard 500 Index Fund"
                        ),
                        go.Scatter(
                            x=df_graph['Date'],
                            y=df_graph['MSCI EAFE Index Fund (ETF)'],
                            line={"color": "rgb(255, 225, 53)"},
                            mode="lines",
                            name="MSCI EAFE Index Fund (ETF)"
                        )
                    ],
                    'layout': go.Layout(
                        autosize=False,
                        width=700,
                        height=200,
                        font={
                            "family": "Raleway",
                            "size": 10
                        },
                        margin={
                            "r": 40,
                            "t": 40,
                            "b": 30,
                            "l": 40
                        },
                        showlegend=True,
                        titlefont={
                            "family": "Raleway",
                            "size": 10
                        },
                        xaxis={
                            "autorange": True,
                            "range": ["2007-12-31", "2018-03-06"],
                            "rangeselector": {"buttons": [
                                {
                                    "count": 1,
                                    "label": "1Y",
                                    "step": "year",
                                            "stepmode": "backward"
                                },
                                {
                                    "count": 3,
                                    "label": "3Y",
                                    "step": "year",
                                            "stepmode": "backward"
                                },
                                {
                                    "count": 5,
                                    "label": "5Y",
                                    "step": "year"
                                },
                                {
                                    "count": 10,
                                    "label": "10Y",
                                    "step": "year",
                                            "stepmode": "backward"
                                },
                                {
                                    "label": "All",
                                    "step": "all"
                                }
                            ]},
                            "showline": True,
                            "type": "date",
                                    "zeroline": False
                        },
                        yaxis={
                            "autorange": True,
                            "range": [18.6880162434, 278.431996757],
                            "showline": True,
                            "type": "linear",
                                    "zeroline": False
                        }
                    )
                },
                config={
                    'displayModeBar': False
                }
            )
        ], className="twelve columns")

    ], className="row ")


def page_page2_row3():
    return html.Div([

        html.Div([
            html.H6(["Average annual returns--updated \
                monthly as of 02/28/2018"],
                    className="gs-header gs-table-header tiny-header"),
            html.Table(make_dash_table(df_avg_returns),
                       className="tiny-header")
        ], className=" twelve columns"),

    ], className="row ")


def page_page2_row4():
    return html.Div([
        html.Div([
            html.H6(["After-tax returns--updated quarterly as of 12/31/2017"],
                    className="gs-header gs-table-header tiny-header"),
            html.Table(make_dash_table(df_after_tax),
                       className="tiny-header")
        ], className=" twelve columns"),

    ], className="row ")


def page_page2_row5():
    return html.Div([
        html.Div([
            html.H6(["Recent investment returns"],
                    className="gs-header gs-table-header tiny-header"),
            html.Table(make_dash_table(df_recent_returns),
                       className="tiny-header")
        ], className=" twelve columns"),

    ], className="row ")


def page_page2_content():
    return page_contents([
        page_page2_row1(),
        page_page2_row2(),
        page_page2_row3(),
        page_page2_row4(),
        page_page2_row5(),
    ])
    # return html.Div([
    #     print_button(),
    #     html.Div([
    #         page_header(),
    #         page_page2_row1(),
    #         page_page2_row2(),
    #         page_page2_row3(),
    #         page_page2_row4(),
    #         page_page2_row5(),
    #     ], className="subpage")
    # ], className="page")
