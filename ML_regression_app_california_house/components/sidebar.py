
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

sidebar_style = {
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "16rem",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
            }
sidebar = html.Div(
    [
        html.H5("California House", className="text-center display-5"),
        html.Hr(),
        html.P(
            "App - ML regression  : Predicting median district prices", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Data viz", href="/dataviz", active="exact"),
                dbc.NavLink("Ml regression", href="/regression", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=sidebar_style,
)