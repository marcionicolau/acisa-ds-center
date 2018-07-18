# coding: utf-8

import os
from random import randint

import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Event, Input, Output, State
from flask import Flask
from DashContents import main_components, main_layout

USERNAME_PASSWORD_PAIRS = [
    ['Administrator', 'adm123'],
    ['JamesBond', '007']
]


# Setup app
server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return main_layout.overview
    elif pathname == '/price-performance':
        return main_layout.pricePerformance
    elif pathname == '/portfolio-management':
        return main_layout.portfolioManagement
    elif pathname == '/fees':
        return main_layout.feesMins
    elif pathname == '/distributions':
        return main_layout.distributions
    elif pathname == '/news-and-reviews':
        return main_layout.newsReviews
    elif pathname == '/full-view':
        return main_layout.overview,
        main_layout.pricePerformance,
        main_layout.portfolioManagement,
        main_layout.feesMins,
        main_layout.distributions,
        main_layout.newsReviews
    else:
        return main_layout.noPage


lst_css = ["https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.css",
           'https://codepen.io/chriddyp/pen/bWLwgP.css',
           "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
           "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
           "//fonts.googleapis.com/css?family=Raleway:400,300,600",
           "https://codepen.io/bcd/pen/KQrXdb.css",
           "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

lst_js = ["https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.js",
          "https://code.jquery.com/jquery-3.2.1.min.js",
          "https://codepen.io/bcd/pen/YaXojL.js"]

for css in lst_css:
    app.css.append_css({"external_url": css})

for js in lst_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
