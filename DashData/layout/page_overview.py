# encoding: utf-8

import dash_html_components as html
import dash_core_components as dcc
from DashData.components.layout import (make_dash_table,
                                        page_contents)

from DashData.datasets.all_data import df_fund_facts, df_price_perf
import plotly.graph_objs as go


def page_overview_row3():
    return html.Div([
        html.Div([
                    html.H6(u"Apresentação",
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    html.P("\
                            Passo Fundo é a maior cidade do Norte do Rio \
                            Grande do Sul e a 6ª maior economia do Estado. \
                            Considerada cidade média, tem população estimada \
                            pelo IBGE (2017) em 198.799 habitantes. \
                            O valor total do PIB alcançou os R$7,8 bilhões e \
                            a renda per capita é de R$ 39.737,73. \
                            Os dados são relativos ao ano de 2015. A cidade é \
                            conhecida como \"Capital do Planalto Médio\", \
                            \"Capital Nacional da Literatura\" e \
                            \"Capital do Norte\". Possui um grande número de \
                            edifícios, sendo uma das cidades mais densas do \
                            Estado.")
                    ], className="six columns"),
        html.Div([
            html.H6(["Fund Facts"],
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(df_fund_facts))
        ], className="six columns"),

    ], className="row ")


def page_overview_row4():
    return html.Div([
        html.Div([
            html.H6('Average annual performance',
                    className="gs-header gs-text-header padded"),
            dcc.Graph(
                id="graph-1",
                figure={
                    'data': [
                        go.Bar(
                            x=["1 Year", "3 Year", "5 Year",
                               "10 Year", "41 Year"],
                            y=["21.67", "11.26", "15.62", "8.37", "11.11"],
                            marker={
                                "color": "rgb(53, 83, 255)",
                                "line": {
                                    "color": "rgb(255, 255, 255)",
                                    "width": 2
                                }
                            },
                            name="500 Index Fund"
                        ),
                        go.Bar(
                            x=["1 Year", "3 Year", "5 Year",
                               "10 Year", "41 Year"],
                            y=["21.83", "11.41", "15.79", "8.50"],
                            marker={
                                "color": "rgb(255, 225, 53)",
                                "line": {
                                    "color": "rgb(255, 255, 255)",
                                    "width": 2
                                }
                            },
                            name="S&P 500 Index"
                        ),
                    ],
                    'layout': go.Layout(
                        autosize=False,
                        bargap=0.35,
                        font={
                            "family": "Raleway",
                            "size": 10
                        },
                        height=200,
                        hovermode="closest",
                        legend={
                            "x": -0.0228945952895,
                            "y": -0.189563896463,
                            "orientation": "h",
                            "yanchor": "top"
                        },
                        margin={
                            "r": 0,
                            "t": 20,
                            "b": 10,
                            "l": 10
                        },
                        showlegend=True,
                        title="",
                        width=340,
                        xaxis={
                            "autorange": True,
                            "range": [-0.5, 4.5],
                            "showline": True,
                            "title": "",
                            "type": "category"
                        },
                        yaxis={
                            "autorange": True,
                            "range": [0, 22.9789473684],
                            "showgrid": True,
                            "showline": True,
                            "title": "",
                            "type": "linear",
                                    "zeroline": False
                        }
                    )
                },
                config={
                    'displayModeBar': False
                }
            )
        ], className="six columns"),

        html.Div([
            html.H6("Hypothetical growth of $10,000",
                    className="gs-header gs-table-header padded"),
            dcc.Graph(
                id="grpah-2",
                figure={
                    'data': [
                        go.Scatter(
                            x=["2008", "2009", "2010", "2011", "2012",
                                       "2013", "2014", "2015", "2016",
                                       "2017", "2018"],
                            y=["10000", "7500", "9000", "10000", "10500",
                               "11000", "14000", "18000", "19000", "20500",
                               "24000"],
                            line={"color": "rgb(53, 83, 255)"},
                            mode="lines",
                            name="500 Index Fund Inv"
                        )
                    ],
                    'layout': go.Layout(
                        autosize=False,
                        title="",
                        font={
                            "family": "Raleway",
                            "size": 10
                        },
                        height=200,
                        width=340,
                        hovermode="closest",
                        legend={
                            "x": -0.0277108433735,
                            "y": -0.142606516291,
                            "orientation": "h"
                        },
                        margin={
                            "r": 20,
                            "t": 20,
                            "b": 20,
                            "l": 50
                        },
                        showlegend=True,
                        xaxis={
                            "autorange": True,
                            "linecolor": "rgb(0, 0, 0)",
                            "linewidth": 1,
                            "range": [2008, 2018],
                            "showgrid": False,
                            "showline": True,
                            "title": "",
                            "type": "linear"
                        },
                        yaxis={
                            "autorange": False,
                            "gridcolor": "rgba(127, 127, 127, 0.2)",
                            "mirror": False,
                            "nticks": 4,
                            "range": [0, 30000],
                            "showgrid": True,
                            "showline": True,
                            "ticklen": 10,
                            "ticks": "outside",
                            "title": "$",
                            "type": "linear",
                                    "zeroline": False,
                                    "zerolinewidth": 4
                        }
                    )
                },
                config={
                    'displayModeBar': False
                }
            )
        ], className="six columns"),

    ], className="row ")


def page_overview_row5():
    return html.Div([
        html.Div([
            html.H6('Price & Performance (%)',
                    className="gs-header gs-table-header padded"),
            html.Table(make_dash_table(df_price_perf))
        ], className="six columns"),

        html.Div([
            html.H6("Risk Potential",
                    className="gs-header gs-table-header padded"),
            dcc.Graph(
                id='graph-3',
                figure={
                    'data': [
                        go.Scatter(
                            x=["0", "0.18", "0.18", "0"],
                            y=["0.2", "0.2", "0.4", "0.2"],
                            fill="tozerox",
                            fillcolor="rgba(31, 119, 180, 0.2)",
                            hoverinfo="none",
                            line={"width": 0},
                            mode="lines",
                            name="B",
                            showlegend=False
                        ),
                        go.Scatter(
                            x=["0.2", "0.38", "0.38", "0.2", "0.2"],
                            y=["0.2", "0.2", "0.6", "0.4", "0.2"],
                            fill="tozerox",
                            fillcolor="rgba(31, 119, 180, 0.4)",
                            hoverinfo="none",
                            line={"width": 0},
                            mode="lines",
                            name="D",
                            showlegend=False
                        ),
                        go.Scatter(
                            x=["0.4", "0.58", "0.58", "0.4", "0.4"],
                            y=["0.2", "0.2", "0.8", "0.6", "0.2"],
                            fill="tozerox",
                            fillcolor="rgba(31, 119, 180, 0.6)",
                            hoverinfo="none",
                            line={"width": 0},
                            mode="lines",
                            name="F",
                            showlegend=False
                        ),
                        go.Scatter(
                            x=["0.6", "0.78", "0.78", "0.6", "0.6"],
                            y=["0.2", "0.2", "1", "0.8", "0.2"],
                            fill="tozerox",
                            fillcolor="rgb(31, 119, 180)",
                            hoverinfo="none",
                            line={"width": 0},
                            mode="lines",
                            name="H",
                            showlegend=False
                        ),
                        go.Scatter(
                            x=["0.8", "0.98", "0.98", "0.8", "0.8"],
                            y=["0.2", "0.2", "1.2", "1", "0.2"],
                            fill="tozerox",
                            fillcolor="rgba(31, 119, 180, 0.8)",
                            hoverinfo="none",
                            line={"width": 0},
                            mode="lines",
                            name="J",
                            showlegend=False
                        ),
                    ],
                    'layout': go.Layout(
                        title="",
                        annotations=[
                            {
                                "x": 0.69,
                                "y": 0.6,
                                "font": {
                                    "color": "rgb(31, 119, 180)",
                                    "family": "Raleway",
                                    "size": 30
                                },
                                "showarrow": False,
                                "text": "<b>4</b>",
                                        "xref": "x",
                                        "yref": "y"
                            },
                            {
                                "x": 0.0631034482759,
                                "y": -0.04,
                                "align": "left",
                                "font": {
                                    "color": "rgb(44, 160, 44)",
                                    "family": "Raleway",
                                    "size": 10
                                },
                                "showarrow": False,
                                "text": "<b>Less risk<br>Less reward</b>",
                                        "xref": "x",
                                        "yref": "y"
                            },
                            {
                                "x": 0.92125,
                                "y": -0.04,
                                "align": "right",
                                "font": {
                                    "color": "rgb(214, 39, 40)",
                                    "family": "Raleway",
                                    "size": 10
                                },
                                "showarrow": False,
                                "text": "<b>More risk<br>More reward</b>",
                                        "xref": "x",
                                        "yref": "y"
                            }
                        ],
                        autosize=False,
                        height=200,
                        width=340,
                        hovermode="closest",
                        margin={
                            "r": 10,
                            "t": 20,
                            "b": 80,
                            "l": 10
                        },
                        shapes=[
                            {
                                "fillcolor": "rgb(255, 255, 255)",
                                "line": {
                                    "color": "rgb(31, 119, 180)",
                                    "width": 4
                                },
                                "opacity": 1,
                                "type": "circle",
                                        "x0": 0.621,
                                        "x1": 0.764,
                                        "xref": "x",
                                        "y0": 0.135238095238,
                                        "y1": 0.98619047619,
                                        "yref": "y"
                            }
                        ],
                        showlegend=True,
                        xaxis={
                            "autorange": False,
                            "fixedrange": True,
                            "range": [-0.05, 1.05],
                            "showgrid": False,
                            "showticklabels": False,
                            "title": "<br>",
                            "type": "linear",
                                    "zeroline": False
                        },
                        yaxis={
                            "autorange": False,
                            "fixedrange": True,
                            "range": [-0.3, 1.6],
                            "showgrid": False,
                            "showticklabels": False,
                            "title": "<br>",
                            "type": "linear",
                                    "zeroline": False
                        }
                    )
                },
                config={
                    'displayModeBar': False
                }
            )
        ], className="six columns")
    ], className="row ")


def page_overview_content():
    return page_contents(
        page_overview_row3(),
        page_overview_row4(),
        page_overview_row5()
    )
