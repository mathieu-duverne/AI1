# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:05:50 2021

@author: straw
"""
import os
from dash.dependencies import Input, Output, State
from app import app
from layouts import parse_contents, save_file
import joblib
from skimage.io import imread
from skimage.transform import resize
import base64
import os
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory
import dash
import dash_core_components as dcc
import dash_html_components as html

from transformers import RGB2GrayTransformer, HogTransformer


UPLOAD_DIRECTORY = "/upload"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


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
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]

# @app.callback(Output('output-image-upload', 'children'),
#               Input('upload-image', 'contents'),
#               State('upload-image', 'filename'))
# def update_picture(list_of_contents, list_of_names):
#     if list_of_contents is not None and list_of_names is not None:
#         children = [
#             parse_contents(c, n) for c, n in
#             zip(list_of_contents, list_of_names)]
#         return children

# @app.callback(Output('output-prediction', 'children'),
#               Input('upload-image', 'contents'),
#               State('upload-image', 'filename'))
# def update_prediction(list_of_contents, list_of_names):
#     directory = 'Output\Mimoun'
#     if list_of_contents is not None and list_of_names is not None:
#         for content, name in zip(list_of_contents, list_of_names):
#             files_in_dir = os.listdir(directory)
#             exts = {".jpg", ".png", ".gif"}
#             filtered_files = [file for file in files_in_dir if any(file.endswith(s) for s in exts)]
#             for img in filtered_files:
#                 if len(filtered_files) >= 1:
#                     path_to_file = os.path.join(directory,img)
#                     os.remove(path_to_file)
#             save_file(name, content)
    
#     width = 80
#     height = 80
#     images = []
#     for file in os.listdir(directory):
#         file = imread(os.path.join(directory, file), as_gray=False)
#         file = resize(file, (width, height))
#         images.append(file)
#     images.append(images[0])  
#     model = joblib.load('output/models/hog_models.pkl')         
#     prediction = model.predict(images)
#     return prediction[0]

# @app.callback(
#     Output('textarea-state-example-output', 'children'),
#     Input('textarea-state-example-button', 'n_clicks'),
#     State('textarea-state-example', 'value'))
# def update_query(n_clicks, value):
#     if n_clicks > 0:
#         return 'You have entered: \n{}'.format(value)









