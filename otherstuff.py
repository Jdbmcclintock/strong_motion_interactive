import requests
import pandas as pd
import numpy as np


def quake_info(quakeid):
    quake_info = requests.get("http://api.geonet.org.nz/quake/" + quakeid).json()
    return quake_info


df = pd.read_csv('all_quakes_2015-2020.csv')
"""
print(quake_info(df.iloc[0]['ID'])['features'][0]['geometry']['coordinates'][0])
idlist = df.ID.tolist()
lat,lon = [],[]
for quake in idlist:
    lon.append(quake_info(quake)['features'][0]['geometry']['coordinates'][0])
    lat.append(quake_info(quake)['features'][0]['geometry']['coordinates'][1])

df["EQ_lat"] = lat
df["EQ_lon"] = lon
df.to_csv("with_quake_info_2020.csv")
""""
#df = pd.read_csv("with_quake_info.csv")
#print(df.head())
#quakesonly = df.drop_duplicates(subset = "ID")
def fetch_strong(id, main_df):
    relevant_rows = main_df[main_df["ID"] == id]
    return relevant_rows

#banana = fetch_strong("2015p012816",df)

banana = pd.read_csv("with_quake_info_2020.csv")

banana["max_percent"] = banana[[ 'PGA Vertical (%g)', 'PGA Horiz_1 (%g)', 'PGA Horiz_2 (%g)',]].max(axis=1)
banana["max pga"] = banana["max_percent"] / 100
#print(fetch_strong("2015p012816",df).keys())
#print(banana[[ 'PGA Vertical (%g)', 'PGA Horiz_1 (%g)', 'PGA Horiz_2 (%g)', "max"]])

pga_conditions = [(banana["max pga"] <=0.002),
                  (banana["max pga"] > 0.002) & (banana["max pga"] <= 0.05),
                  (banana["max pga"] > 0.05) & (banana["max pga"] <= 0.1),
                  (banana["max pga"] > 0.1) & (banana["max pga"] <= 0.2),
                  (banana["max pga"] > 0.2) & (banana["max pga"] <= 0.5),
                  (banana["max pga"] > 0.5) & (banana["max pga"] <= 1),
                  (banana["max pga"] >=1)]
pga_label = ["0.002", "0.002 - 0.05", "0.05 - 0.1", "0.1 - 0.2", "0.2 - 0.5", "0.5 - 1", "> 1"]
size_bracket = [1, 2, 3, 4, 5, 6, 7]
colors = ["#989898", "#eff3ff", "#dbdaeb", "#b5c5df", "#3a90c0", "#096ca6", "#08519c"]



banana["pg_bracket"] = np.select(pga_conditions, pga_label)
banana["pga_size"] = np.select(pga_conditions, size_bracket)
banana["color"] = np.select(pga_conditions, colors)

banana.to_csv("with_quake_info_2020.csv")