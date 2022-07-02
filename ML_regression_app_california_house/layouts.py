from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn import tree, neighbors
from sklearn.ensemble import ExtraTreesRegressor 

from components.Control import Control
from components.sidebar import sidebar
from data.Cleaningdata import Clean_and_transform_data

df = pd.read_csv('data/housing.csv')

# get interest col for control
col = ['median_income', 'population', 'median_house_value', 'households', 'housing_median_age']

all_col = ['latitude', 'longitude', 'total_rooms', 'total_bedrooms', 'ocean_proximity', 'median_income', 'population', 'median_house_value', 'households', 'housing_median_age']

data = Clean_and_transform_data(df)
data.clean_and_transform_data()

# ---- layout Dashboard ---- #
control = Control()
control_dashboard_columns = control.control_dashboard_html(all_col)
# ---- layout Dashboard ---- #

# ---- MAAP layout DATAVIZ ---- #
control_california_map_html = control.control_california_map_html(col)

# make a row with controller and graph
row_control_and_california_map = html.Div(
                    [
                        dbc.Col(control_california_map_html, md=12), 
                        dbc.Col(dcc.Graph(id="california_map"), md=12)
                    ],
                    )   
row_control_hist_column = html.Div(
                    [
                        dbc.Col(control_dashboard_columns, md=12), 
                        dbc.Col(dcc.Graph(id="hist_col"), md=12)
                    ],
                    )    

# ---- MAAP layout DATAVIZ ---- #

# ---- layout regression ---- #

features_importance = {'population' : 0.04805861, "households": 0.05273876, "housing_median_age":0.06898811, "longitude":0.10547412, "latitude":0.11206104, "diag_coord":0.25216602,  "income_cat":0.36051334,}

# [0.10547412, 0.11206104, 0.06898811, 0.04805861, 0.05273876,
#        0.36051334, 0.25216602])

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("19675 district in california", className="card-title"),
            html.P("Dataset"),
            # dbc.Button("Go somewhere", color="primary"),
        ]
    )
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5(str(data.len_train) + " / " + str(data.len_test), className="card-title"),
            html.P("70% Training / 30% Testing split"),
            # dbc.Button("Go somewhere", color="primary"),
        ]
        
    ), color="primary", inverse=True,
)

cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(third_card, width=8),
    ]
)

row_dashboard = dbc.Row(
    [
            html.H5("7 Features importances", className="card-title"),
        dbc.Col(
            dcc.Checklist(id = 'check_lists',
                           options = [{'label': name, 'value': name}for name, value in features_importance.items()],
                           value = [i for i, e in features_importance.items()],
                           labelStyle={'display': 'block'},
                           className = 'dcc_compon p-2'), width=3),
        dbc.Col(dcc.Graph(id="hist_feature"), width=9)
    ]
)


models = {'Decision Tree': tree.DecisionTreeRegressor, 'Extra Tree Regression': ExtraTreesRegressor}
control_mlregression = control.control_ml_regression(models)
# ---- layout regression ---- #

# ---- CONTENT PER page ---- #
content_ml_regression = html.Div(children=[html.H6("models machin learning regression", className="display-6"), control_mlregression], id='page-content')

content_dataviz = html.Div(children=[html.H2("California map"),row_control_and_california_map], id='page-content')

content_dashboard = html.Div(children=[cards,html.Hr(),row_dashboard, row_control_hist_column], id='page-content')

# concatener sidebar plus graph voir les callbacks pour les props
dashboard_layout = html.Div([sidebar, content_dashboard])

dataviz_layout = html.Div([sidebar, content_dataviz])

regression_layout = html.Div([sidebar, content_ml_regression])