# encoding: utf-8

import dash_html_components as html
import dash_core_components as dcc


LOGO = 'http://www.acisa.org.br/wp-content/uploads/2016/12/acisa_logo1-1.png'


def get_logo():
    logo = html.Div([
        html.Div([
            html.Img(
                src=LOGO,
                height='40', width='130')
        ], className="ten columns padded"),
        html.Div([
            dcc.Link('Geral   ', href='/full-view')
        ], className="two columns page-view no-print")
    ], className="row gs-header")
    return logo


def get_header():
    return html.Div([
        html.Div([
            html.H5(u'ACISA - Central de Dados e Estatísticas \
            sobre o Município'),
            html.H6(u'Passo Fundo/RS'),
        ], className="twelve columns padded"),
    ], className="row gs-header gs-text-header")


def get_menu():
    return html.Div([
        dcc.Link('Geral         ',
                 href='/overview',
                 className="tab first"),
        dcc.Link(u'Socioeconômia        ',
                 href='/price-performance',
                 className="tab"),
        dcc.Link('Serviços          ',
                 href='/portfolio-management',
                 className="tab"),
        dcc.Link('Comércio         ',
                 href='/fees',
                 className="tab"),
        dcc.Link('Indústria         ',
                 href='/fees',
                 className="tab"),
        dcc.Link('Saúde         ',
                 href='/fees',
                 className="tab"),
        dcc.Link('Agricultura           ',
                 href='/distributions',
                 className="tab"),
        dcc.Link(u'Notícias e Análises      ',
                 href='/news-and-reviews',
                 className="tab")

    ], className="row ")


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
    return html.A(['Gerar PDF'],
                  className="button no-print print",
                  style=dict(
                      position='absolute',
                      top='-40',
                      right='0'
    ))


def page_header():
    return [
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ]


def page_contents(content):
    pg_content = content.insert(0, page_header())
    return html.Div([
        print_button(),
        html.Div(pg_content, className="subpage")
    ], className="page")
