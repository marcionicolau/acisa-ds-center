# encoding: utf-8

import dash_html_components as html


def page_404():
    return html.Div([
        html.P(["404 Page not found"])
    ], className="no-page")
