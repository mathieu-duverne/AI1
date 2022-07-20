# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:04:48 2021

@author: straw
"""
import dash
from flask import Flask, send_from_directory
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_html_components as html
from dash.dependencies import Input, Output

import base64
import os
from skimage.io import imread
from skimage.transform import resize
import joblib
from transformers import RGB2GrayTransformer, HogTransformer

import shutil


UPLOAD_DIRECTORY = "C:/Users/Tetar/Desktop/AI1/image_classification/upload/"

if not os.path.exists(UPLOAD_DIRECTORY): os.makedirs(UPLOAD_DIRECTORY)
else: shutil.rmtree('upload')

BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/minty/bootstrap.min.css"


# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=[BS])
server = app.server
app.title = "Image classifier"

app.layout = html.Div(children=[
    html.Div(children=[html.H1('Welcome on my animals classifier using Support Vector Machine')], style={'text-align': 'center', 'color': 'black', 'padding': '10px'}),
    html.Br(),
    
dbc.Jumbotron(children=[
    html.Div(className="display-left", children=[html.P('Import images and await a response of image classifier : ')], style={'text-align': 'left', 'color': 'black', 'padding': '10px'}),
    html.Br(),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'glisser-déposer ou ',
            html.A('sélectionner des fichiers')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'color': 'red',
        },
        # Allow multiple files to be uploaded
        multiple=True
    ), ]), html.Div(id="file-list"), ])
    

def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))

def uploaded_files():
    if not os.path.exists(UPLOAD_DIRECTORY): os.makedirs(UPLOAD_DIRECTORY)
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    


    """Save uploaded files and regenerate the file list."""
    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return html.P(
            "No files available for classify.",
            style={"color": "#FFC107"}  )
    else:
        directory = 'upload/'
        width = 80
        height = 80
        images = []
        for file in os.listdir(directory):
            file_read = imread(os.path.join(directory, file), as_gray=False)
            file_resize = resize(file_read, (width, height))
            images.append(file_resize)
        images.append(images[0])  
        model = joblib.load('output/hog_sgd_model.pkl')        
        prediction = model.predict(images)
        # print(model.predict_proba(images))
        shutil.copy('upload/'+file, 'archive_classify_image/')

        shutil.rmtree('upload')
        
        response = html.Div(children=[
            html.P(
                   "Your picture is : " + str(prediction[0]),
                    style={"color": "green"}),
            html.Br(),
            html.P(
                "please refresh the page to upload new picture",
                style={"color": "green"}),
        ])


        return response

if __name__ == "__main__":
    app.run_server(debug=True)