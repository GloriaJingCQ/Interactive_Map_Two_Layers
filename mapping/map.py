import folium
import pandas
import json
import io

data_json = io.open("world.json",'r',encoding='utf-8-sig').read()
data = pandas.read_csv('Volcanoes.txt', on_bad_lines='skip')
lat = list(data["LON"])
lon = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
map = folium.Map(location=[50,-123], zoom_start=5,
tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lon,lat, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el)+"m", fill_color=color_producer(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
```

fgp.add_child(folium.GeoJson(data=data_json,style_function=lambda x: {'fillColor':'blue' if x['properties']
['POP2005'] < 10000000
else 'purple' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
