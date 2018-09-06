import folium
map =folium.Map(location=[38.58, -99.09], zoom_start=6,)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

# The above created the Map Html with the co-ordinates (long&Lat) and sets the Zoom status on the Map, it also addes a marker to the map, this is ok for one marker but adding mutiple marks can be problematic.
