import folium

tehran = folium.Map(location=[35.80814661987119, 51.27057378625933], zoom_start=10)

folium.Marker(location=[35.6904546123279, 51.297653787424345], popup='Airport', icon=folium.Icon(icon='plane', prefix='fa')).add_to(tehran)

top_left = [35.90,51.10]
bottom_right = [35.50,51.70]

rect = folium.Rectangle(
    bounds=[top_left, bottom_right],
    fill=True,
    fill_color='green',
    color='blue',
    opacity=0.5,
    fill_opacity=0.2
).add_to(tehran)

# Display map
print(tehran)
