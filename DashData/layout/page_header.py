# encoding: utf-8

import dash_html_components as html
from DashData.components.layout import (get_header, get_logo,
                                        get_menu)


def page_header():
    return [
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ]
