import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests

from dash.dependencies import Input, Output

USERNAME_PASSWORD_PAIRS = [
    ['Administrator', 'adm123'],
    ['JamesBond', '007']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server

app.layout = html.Div([
    html.Div([
        html.Iframe(src='https://www.flightradar24.com',
                    height=500, width=1200)
    ]),
    html.Div([
        html.Pre(
            id='counter_text',
            children='Active flights worldwide:'
        ),
        dcc.Graph(
            id='live-update-graph',
            style={'width': 1200}
        ),
        dcc.Interval(
            id='interval-component',
            interval=6000,  # 6000 milliseconds = 6 seconds
            n_intervals=0
        )
    ]),
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i: str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width': '50%'})

counter_list = []


@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # A fake header is necessary to access the site:
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return 'Active flights worldwide: {}'.format(counter)


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    fig = go.Figure(
        data=[go.Scatter(
            x=list(range(len(counter_list))),
            y=counter_list,
            mode='lines+markers'
        )])
    return fig


@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]


if __name__ == '__main__':
    app.run_server()
