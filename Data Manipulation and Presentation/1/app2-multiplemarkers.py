import folium
map =folium.Map(location=[38.58, -99.09], zoom_start=6,)

fg = folium.FeatureGroup(name="My Map")
pop = 0

for coordinates in [[38.2, -99.1], [37.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

#So by adding a for loop to this you can iterate through the list of coordinates easily and once run adds them to the map.
#The issue with this is you cannot add a 1000 coordinates to a list in python, we need to find a better way
