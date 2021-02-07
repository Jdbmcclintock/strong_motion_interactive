import pandas as pd
import plotly.express as px

df_full = pd.read_csv("quakes_with_bearings.csv")
df_slice = df_full[0:100]

fig = px.scatter_polar(df_slice, r = 'Epic. Dist.(km)', theta = "bearing", size = 'max pga')

fig.show()

"""
fig = px.line(df_slice, x = 'Epic. Dist.(km)', y = ['PGA Vertical (mm/s/s)',
                                                       'PGA Horiz_1 (mm/s/s)',
                                                       'PGA Horiz_2 (mm/s/s)'])
print(df_slice.keys())
fig.show()"""

from numpy import arctan2, random, sin, cos, degrees

import math


"""
def compass_bearing(point_1, point_2):
    lat1 = math.radians(point_1[0])
    lat2 = math.radians(point_2[0])

    dL = math.radians(point_2[1] - point_1[1])

    x = math.sin(dL) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dL)

    initial_bearing = math.atan2(x, y)

    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

list_of_bearings  = [compass_bearing((df_full.iloc[i]["EQ_lat"], df_full.iloc[i]["EQ_lon"]),
                                     (df_full.iloc[i]["Site Latitude"], df_full.iloc[i]["Site Longitude"]))
                     for i in range(len(df_full))]

df_full["bearing"] = list_of_bearings
print(df_full[["EQ_lat", "EQ_lon", "Site Latitude", "Site Longitude", "bearing"]])
df_full.to_csv("quakes_with_bearings.csv")"""
