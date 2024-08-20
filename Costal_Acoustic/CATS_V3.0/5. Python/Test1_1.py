import folium

map = folium.Map(location=[37.7833, -122.4167], zoom_start=10)

# html_str = folium.embed.js(map)

map.save('test1_1123.html')