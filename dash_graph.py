import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import requests
from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.Div(className='parent', children=[

        html.Div(className='pD', children=[

           dcc.Dropdown(id='size', options=[
                {'label': 'Small', 'value': 'small'},
                {'label': 'Medium', 'value': 'medium'},
                {'label': 'Large', 'value': 'large'}
            ])

        ]),

        html.Div(className='submit', children=[

            html.Button('Submit', id='submit', n_clicks=0)

        ]),

        html.Div(className='graph_box cD', children=[dcc.Graph(id='graph')])

    ]),

])

"""app.layout = html.Div(className='row', style =  {"height":"100%"} ,children=[
                        html.H1("poo poo"),
                     html.Div(children=[
        dcc.Graph(id="graph1", figure = fig, style={'width':'50%','height':'80%',
                                                    'display': 'inline-block'}),
        dcc.Graph(id="graph2", figure= fig2, style={'width':'50%','height':'80%',
                                                    'display': 'inline-block'})
    ])
])"""


df = pd.read_csv("with_quake_info.csv")

quakesonly = df.drop_duplicates(subset = "ID")

fig = go.Figure(go.Scattermapbox(
                lat = quakesonly["EQ_lat"], lon = quakesonly["EQ_lon"],
                mode= 'markers',
                marker = go.scattermapbox.Marker(color='red',
                                                 size = [i**1.5 * 2 for i in quakesonly["Magnitude"]],
                                                  )))

fig.update_layout(
    height = 1000,
    hovermode='closest',
    margin = dict(l = 0, r = 0, t = 0, b = 0),
    mapbox_style="open-street-map",
    mapbox=dict(
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-40.2,
            lon=174.8
        ),
        pitch=0,
        zoom=4.5
    )

)
""""
fig2 = go.Figure(go.Scattermapbox(mode= 'markers',
                 marker = go.scattermapbox.Marker(color='red',
                                                 size = 50,
                                                  )))

fig2.update_layout(
    height = 1000,
    hovermode='closest',
    margin = dict(l = 0, r = 0, t = 0, b = 0),
    mapbox_style="open-street-map",
    mapbox=dict(
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-40.2,
            lon=174.8
        ),
        pitch=0,
        zoom=4.5
    ))"""

dcc.Graph(
    id='graph',
    figure={}
)

@app.callback(
    Output('graph', 'figure'),
    [Input('submit', 'n_clicks')],
    [State('size', 'value')]
)
def update_chart(clicks, size):
    if clicks:
        return {'data': [{'x': np.random.randint(0, 100, 1000), 'type': 'histogram'}]}
    else:
        return {'data': [], 'type': 'histogram'}

if __name__ == "__main__":
    app.run_server(debug=True)