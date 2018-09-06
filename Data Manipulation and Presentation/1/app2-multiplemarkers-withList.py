#Functions to import
import folium
import pandas

#Data to read from
data = pandas.read_csv("volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#Function for Colour Coding the Popup Markers to Elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'

#Creating the Map Starting Point
map =folium.Map(location=[38.58, -99.09], zoom_start=2,)

fg = folium.FeatureGroup(name="Volcanoes in North America")

#Adding CircleMarkers to the Map with the details of the Name, Elevation in Metres
for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius = 6, popup=folium.Popup((nm)+"," +" "+"Elevation:"+ str(el) +"m",  parse_html=True), fill_color=color_producer(el), color = color_producer(el), fill=True, fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'yellow'}))


map.add_child(fg)

#Saves the Map to a HTML file locally
map.save("Map1.html")
