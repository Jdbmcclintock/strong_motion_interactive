import urllib.request as request
import pandas as pd
from bs4 import BeautifulSoup
import io


def get_csv_name(year):
    generic_ftp_name = "ftp://ftp.geonet.org.nz/strong/processed/Summary/"
    ftp_link = request.urlopen(generic_ftp_name + str(year))
    soup = BeautifulSoup(ftp_link, 'lxml')
    soupstring = soup.body()[0].text
    string_io = io.StringIO(soupstring)
    table = pd.read_table(string_io, delim_whitespace = True, names = ["blah", "blah2", "blah3","blah4",
                                                                       "blah5", "blah6", "blah7", "blah8", "CSV_link"])
    list_of_csv = table.CSV_link.tolist()
    quake_id_list = [i[0:11] for i in list_of_csv]
    return list_of_csv

list_of_events = []
for i in range(2015, 2020):
    list_of_events.append(get_csv_name(i))

#print(list_of_events)

def get_csv(event):
    csv = pd.read_csv("ftp://ftp.geonet.org.nz/strong/processed/Summary/" + event[0:4] + "/" + event)
    return csv
#print(list_of_events[0])
list_of_csvs = []
for pull in list_of_events[0]:
    list_of_csvs.append(get_csv(pull))

big_csv = pd.concat(list_of_csvs)
print(big_csv)
big_csv.to_csv("all_quakes.csv")

"""df = get_csv_name(2020)

print(df.CSV_link[0])

list_of_csv = df.CSV_link.tolist()

#csv = pd.read_csv("ftp://ftp.geonet.org.nz/strong/processed/Summary/2020/" + list_of_csv[0])
quake_id_list = [i[0:11] for i in list_of_csv]


print(list_of_csv[0][0:11])"""