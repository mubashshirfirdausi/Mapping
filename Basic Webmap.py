import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
loc = list(data["LOCATION"])


# html = """<h4>Volcano information:</h4>
# Height: %s m
# """

def color_producer(para):
    if para<=1000:
        return "green"
    elif para>1000 and para<=2000:
        return "yellow"
    elif para>2000 and para <=3000:
        return "orange"
    else: return "red"

map = folium.Map(location = [lat[25],lon[25]],zoom_start = 5, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, na, loca in zip(lat, lon, elev, name, loc):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup = f"Name:{na} \n Location:{loca} \n Elevation:{el}m", fill_color = color_producer(el), color = "Grey", fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open('D:\Python Practice\Mapping\world.json','r', encoding = 'utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
print(map)
map.save("Map1.html")
