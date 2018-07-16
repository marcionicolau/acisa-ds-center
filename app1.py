import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

USERNAME_PASSWORD_PAIRS = [
    ['Administrator', 'adm123'],
    ['JamesBond', '0007']
]

app = dash.Dash()
