# coding: utf-8

import dash_html_components as html


def make_dash_table(dataframe, max_rows=10):
    """ Return a Pandas DataFrame as HTML table """
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


def print_button():
    printButton = html.A(['Gerar PDF'], className="button no-print print",
                         style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton
