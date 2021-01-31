import requests
import pandas as pd

"""
def quake_info(quakeid):
    quake_info = requests.get("http://api.geonet.org.nz/quake/" + quakeid).json()
    return quake_info


df = pd.read_csv('all_quakes.csv')

print(quake_info(df.iloc[0]['ID'])['features'][0]['geometry']['coordinates'][0])
idlist = df.ID.tolist()
lat,lon = [],[]
for quake in idlist:
    lon.append(quake_info(quake)['features'][0]['geometry']['coordinates'][0])
    lat.append(quake_info(quake)['features'][0]['geometry']['coordinates'][1])

df["EQ_lat"] = lat
df["EQ_lon"] = lon
df.to_csv("with_quake_info.csv")
"""

df = pd.read_csv("with_quake_info.csv")
print(df.head())
quakesonly = df.drop_duplicates(subset = "ID")
def fetch_strong(id, main_df):
    relevant_rows = main_df[main_df["ID"] == id]
    return relevant_rows

banana = fetch_strong("2015p012816",df)
banana["max"] = banana[[ 'PGA Vertical (%g)', 'PGA Horiz_1 (%g)', 'PGA Horiz_2 (%g)',]].max(axis=1)
print(fetch_strong("2015p012816",df).keys())
print(banana[[ 'PGA Vertical (%g)', 'PGA Horiz_1 (%g)', 'PGA Horiz_2 (%g)', "max"]])

