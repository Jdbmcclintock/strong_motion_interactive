import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# example measurement stations
lats = [41.434760, 38.436662]
lons = [-105.925030, -88.962141]
text = ['red', 'blue']

def fetch_strong(id, main_df):
    relevant_rows = main_df[main_df["ID"] == id]
    return relevant_rows

app = dash.Dash()
df = pd.read_csv("with_quake_info.csv")

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id="mapbox",
            figure={
                "data": [
                    dict(
                        type="scattermapbox",
                        lat=df["EQ_lat"],
                        lon=df["EQ_lon"],
                        mode="markers",
                        marker={'size': '14'},
                        text=df["ID"]
                    )
                ],
                "layout": dict(
                    autosize=True,
                    hovermode="closest",
                    margin=dict(l=0, r=0, t=0, b=0),
                    mapbox=dict(
                        #accesstoken=mapbox_access_token,
                        bearing=0,
                        center=dict(lat=-40.2,
                                    lon=174.8),
                        style="open-street-map",
                        pitch=0,
                        zoom=3.5,
                        layers=[]
                    )
                )
            },
            style={'width':'45%','height':'80%',
                   'display': 'inline-block'}
        )
    ]),
    # text container
    ##"""html.Div([
      #  html.P(id='station_id',
       #        style={'fontSize': '12px'})])""",
    # graph container
    html.Div([
        dcc.Graph(
            id="mapbox2",
            figure={
                "data": [
                    dict(
                        type="scattermapbox",
                        mode="markers",
                        marker={'size': '14'},
                        text=text
                    )
                ],
                "layout": dict(
                    autosize=True,
                    hovermode="closest",
                    margin=dict(l=0, r=0, t=0, b=0),
                    mapbox=dict(
                        # accesstoken=mapbox_access_token,
                        bearing=0,
                        center=dict(lat=-40.2,
                                    lon=174.8),
                        style="open-street-map",
                        pitch=0,
                        zoom=3.5,
                        layers=[]
                    )
                )
            }, style={'width':'45%','height':'80%',
                   'display': 'inline-block'})])

],style =  {"width":"100%"}, className="row")


@app.callback(
    Output('mapbox2', 'figure'),
    [Input('mapbox', 'clickData')])
def plot_basin(selection):
    if selection is None:
        return {}
    else:
        lat = fetch_strong(selection['points'][0]['text'], df)["Site Latitude"]
        lon = fetch_strong(selection['points'][0]['text'], df)["Site Longitude"]

        # depending on the station text use different color for line

        data = [go.Scattermapbox(
            lat=lat,
            lon=lon,
            opacity=0.8,
            name="Graph"
        )]
        layout = go.Layout(height = 1000,
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
                zoom=4.5 ))

        return {'data': data, 'layout': layout}

if __name__ == "__main__":
    app.run_server(debug=True)