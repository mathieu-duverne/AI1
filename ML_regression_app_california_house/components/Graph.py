from pandas import DataFrame
import plotly.express as px
from dash import Input, Output, dcc, html



class Graph:
    
    def __init__(self, df):
        self.df = df
    
    def california_map(self, color, size, opacity):
        fig = px.scatter_mapbox(self.df,
                        lat="latitude",
                        lon="longitude",
                        color=color,
                        size=size,
                        opacity=opacity,
                        hover_name="ocean_proximity",
                        hover_data=["population", "median_income"],
                        color_continuous_scale=px.colors.sequential.Plasma,
                        zoom=4,
                        width=1000,
                        height=300)
        
        fig.update_layout(mapbox_style="open-street-map")

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        # return html.Div(dcc.Graph(figure=fig, id="california_map"), style={'width' : '100'})
        return fig
    
    def columns_hist(self, col):
        fig = px.histogram(self.df, x=col)
        return fig
    
    def col_hist(self, array_name):
        features_importance = {'population' : 0.04805861, "households": 0.05273876, "housing_median_age":0.06898811, "longitude":0.10547412, "latitude":0.11206104, "diag_coord":0.25216602,  "income_cat":0.36051334,}
        # print(array_name)
        feature_value = [0.04805861, 0.05273876,0.06898811,0.10547412, 0.11206104, 0.25216602,0.36051334]
        feature_name = ["population", "households","housing_median_age","longitude", "latitude", "diag_coord", "income_cat"]
        
        features_importance = DataFrame({"feature_name" :feature_name, "percentage_use": feature_value})
        
        for index, name  in features_importance.iterrows():
            i= 1
            # print(name)
            if name['feature_name'] not in array_name:
                # print("sisi")
                features_importance.drop(index=index, inplace=True)
            i+=1
        # print(features_importance)
        fig = px.histogram(features_importance, x="feature_name", y="percentage_use")
        return fig
        

        