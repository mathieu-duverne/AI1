from dash.dependencies import Input, Output
from components.Graph import Graph
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import tree, neighbors
from sklearn.ensemble import ExtraTreesRegressor 
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from data.Cleaningdata import Clean_and_transform_data 
from sklearn import metrics

df = pd.read_csv('data/housing.csv')

from app import app

@app.callback(Output("california_map", "figure"), [Input("color", "value"), Input("size", "value"), Input("my-slider", "value")])

def display_row_control_california_map(color, size, opacity):    
        g = Graph(df)
        figure = g.california_map(color, size, opacity)
        return figure

@app.callback(Output("hist_col", "figure"), [Input("columns_hist", "value")])

def display_column_hist(col):    
        g = Graph(df)
        figure = g.columns_hist(col)
        return figure
    
data = Clean_and_transform_data(df)
X_train, y_train, X_test, y_test = data.clean_and_transform_data()
X = data.X
models = {'Decision Tree': tree.DecisionTreeRegressor, 'Extra Tree Regression': ExtraTreesRegressor}

 
@app.callback(
    Output("graphe", "figure"), 
    [Input('model-name', "value")])
def train_and_display(name):
    model = models[name](max_depth=30, random_state=42)
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)
    test = pd.DataFrame({'Predicted':prediction,'Actual':y_test})
    test = test.reset_index()
    test = test.drop(['index'],axis=1)

    fig = px.scatter(test, x="Predicted", y="Actual", trendline="ols", opacity=0.6, trendline_color_override='darkblue')
    
    return fig


features_importance = {'population' : 0.04805861, "households": 0.05273876, "housing_median_age":0.06898811, "longitude":0.10547412, "latitude":0.11206104, "diag_coord":0.25216602,  "income_cat":0.36051334,}


@app.callback(Output("hist_feature", "figure"), [Input("check_lists", "value")])

def display_column_hist(value):    
        g = Graph(df)
        figure = g.col_hist(value)
        return figure