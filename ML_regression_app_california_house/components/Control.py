from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc


class Control:
    def __init__(self) -> None:
        pass
    
    def control_california_map_html(self, col):
        controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("color"),
                dcc.Dropdown(
                    id="color",
                    options=[
                        {"label": c, "value": c} for c in col 
                    ],
                    value="median_house_value",
                ),
            ]
        ),
        html.Div(
            [
                dbc.Label("size"),
                dcc.Dropdown(
                    id="size",
                    options=[
                        {"label": c, "value": c} for c in col 
                    ],
                    value="population",
                ),
            ]
        ),
        dbc.Label("opacity"),
        dcc.Slider(
            id='my-slider',
            min=0,
            max=1,
            step=0.1,
            value=0.6,
            marks={
                0: '0',
                0.2: '0.2',
                0.4: '0.4',
                0.6: '0.6',
                0.8: '0.8'
                },
        ),
        html.Div(id='slider-output-container')
    ],
    body=True,
)
        return controls
    
    def control_dashboard_html(self, col):
        controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("All columns of dataset"),
                dcc.Dropdown(
                    id='columns_hist',
                    options=[
                        {"label": c, "value": c} for c in col 
                    ],
                    value="median_house_value",
                ),
            ]
            
        ),
        ],     style={"width": "18rem"},
)
        return controls
    
    def control_ml_regression(self, models):
        controler_ml = html.Div([
                            dcc.Dropdown(
                                    id='model-name',
                                    options=[{'label': x, 'value': x} for x in models],
                                    value='Decision Tree'
                                ),
                            dcc.Graph(id="graphe"),
                            ])
        return controler_ml