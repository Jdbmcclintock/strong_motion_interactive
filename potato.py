import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px


link = ['https://codepen.io/chriddyp/pen/bWlwgP.css']
app = dash.Dash(__name__, external_stylesheets=link)


57

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as anus
link = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                external_stylesheets=link, meta_tags=[{"content": "width=device-width,initial-scale=1"}])

# example measurement stations
lats = [41.434760, 38.436662]
lons = [-105.925030, -88.962141]
text = ['red', 'blue']

def fetch_strong(id, main_df):
    relevant_rows = main_df[main_df["ID"] == id]
    return relevant_rows

df = pd.read_csv("quakes_with_bearings.csv")
df_dropped_dupes = df.drop_duplicates(subset = "ID")

#layout = go.Layout(margin=dict(t=30, b = 10, l = 10, r = 10))

fig2 = go.Figure(go.Scattermapbox(
        mode = 'markers',
        marker = dict(color='black',
                      size = [i**1.5 * 2 for i in df["pga_size"].tolist()]),
      ))




fig2.update_layout(
    height = 450,
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
    ))

#print(df)


fig = go.Figure(go.Scattermapbox(
                lat = df_dropped_dupes["EQ_lat"], lon = df_dropped_dupes["EQ_lon"],
                mode= 'markers',
                line = dict(color='black', width = 2) ,
                text= df_dropped_dupes["ID"],
                marker = dict(color='rgba(255,99,71,0.85)',
                              size = [i**1.5 * 2 for i in df_dropped_dupes["Magnitude"].tolist()]
                              ),
                )
)


fig.update_layout(
    height = 450,
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
    ))

pga_dist_scat = px.scatter(df[0:100], x = 'Epic. Dist.(km)', y = 'max pga')
pga_dist_scat.update_layout(
    height = 450,
    hovermode='closest',
    margin = dict(l = 0, r = 0, t = 0, b = 0))

polar_plot = px.scatter_polar(df[0:100], r = 'Epic. Dist.(km)', theta = "bearing", size = 'max pga')
polar_plot.update_layout(
    height = 450,
    hovermode='closest',
    margin = dict(l = 0, r = 0, t = 0, b = 0))


app.layout = html.Div([
    html.Div([
            html.Div([
                html.H5('Column 1'),
                dcc.Graph(
                    id="mapbox",
                    figure=fig)],
                    className = 'six columns'),
            html.Div([html.H6(children='Bananatime'),
                  dcc.Graph(id='scat',
                            figure=pga_dist_scat)],
                 className='six columns')],
        className="row"),
    html.Div([
            html.Div([
                html.H5('Column 2'),
                dcc.Graph(
                    id="mapbox2",
                    figure=fig2)],
                    className = 'six columns'),
            html.Div([html.H6(children='Bananatime'),
                  dcc.Graph(id='polar',
                            figure=polar_plot)],
                 className='six columns')],
        className="row"),
                ])





@app.callback([
    Output('mapbox2', 'figure'),
    Output('scat', 'figure')],
    [Input('mapbox', 'clickData')])
def plot_basin(selection):
    if selection is None:
        return fig2
    else:
        lat = fetch_strong(selection['points'][0]['text'], df)["Site Latitude"]
        lon = fetch_strong(selection['points'][0]['text'], df)["Site Longitude"]
        strong_color = fetch_strong(selection['points'][0]['text'], df)["color"]
        strong_size = fetch_strong(selection['points'][0]['text'], df)["pga_size"]
        max_pga_df = fetch_strong(selection['points'][0]['text'], df)["max pga"]
        mag_pga_short_string = ["Pga: " + str(i)[0:4] for i in max_pga_df]
        epic_distance = fetch_strong(selection['points'][0]['text'], df)['Epic. Dist.(km)']
        # depending on the station text use different color for line

        data = [go.Scattermapbox(
            lat=lat,
            lon=lon,
            opacity=1,
            text = mag_pga_short_string,
            marker=dict(color=strong_color,
                        size= [(i+ 1)  * 5 for i in strong_size]
                        ),
            name="Graph"
        )]
        layout = go.Layout(height = 450,
            hovermode='closest',
            margin = dict(l = 0, r = 0, t = 0, b = 0),
            mapbox_style="open-street-map",
            mapbox=dict(
                bearing=0,
                center=go.layout.mapbox.Center(
                    lat=-40.2,
                    lon= 174.8
                ),
                pitch=0,
                zoom=4.5 ))

        return {'data': data, 'layout': layout}

if __name__ == "__main__":
    app.run_server(debug=True)