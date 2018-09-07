import folium
map =folium.Map(location=[51.55, 0.27], zoom_start=6,)

fg = folium.FeatureGroup(name="Footie Tour")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.save("football.html")
