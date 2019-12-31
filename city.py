import pandas as pd
import requests
import time

df = pd.read_csv("Output/island_info.csv")

lats = []
lngs = []

for item in df["latitude"]:
    lats.append(item)

for item in df["longitude"]:
    lngs.append(item)

api_key = "95dae95aa2msh0b071f4b3edb1e6p14600fjsn07c5812c37b8"

citys = []
distances = []

for x in range(len(lats)):
    print(x)
    if lngs[x] < 0:
        
        response = requests.get("https://wft-geo-db.p.rapidapi.com/v1/geo/locations/{0}{1}/nearbyCities?limit=1&minPopulation=1000&radius=10000".format(lats[x],lngs[x]),
         headers={
           "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
           "X-RapidAPI-Key": api_key
         }
        ).json()
    
    else:
        
        response = requests.get("https://wft-geo-db.p.rapidapi.com/v1/geo/locations/{0}+{1}/nearbyCities?limit=1&minPopulation=1000&radius=10000".format(lats[x],lngs[x]),
         headers={
           "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
           "X-RapidAPI-Key": api_key
         }
        ).json()
    
    #print(response)
    city = response['data'][0]['city']
    distance = response['data'][0]['distance']
    
    citys.append(city)
    distances.append(distances)
    
    time.sleep(1)

df['nearest_city'] = citys
df['city_distance'] = distances

df.to_csv("Output/island_info.csv", index = False)