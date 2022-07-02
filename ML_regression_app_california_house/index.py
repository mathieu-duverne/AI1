from dash import Input, Output, dcc, html


from app import app
from layouts import dashboard_layout, dataviz_layout, regression_layout
import callbacks

content_style = { "margin-left": "18rem", "margin-right": "2rem", "padding": "2rem 1rem", }

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content', style=content_style)
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/':
         return dashboard_layout
    elif pathname == '/dataviz':
         return dataviz_layout
    elif pathname == '/regression':
         return regression_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)