import folium

mashhad = folium.Map(location=[36.29633610452868, 59.61219276319479], zoom_start=8)

folium.Marker(location=[36.228414038516235, 59.64655688111786], popup='Airport', icon=folium.Icon(icon='plane', prefix='fa')).add_to(mashhad)

top_left = [35.90,51.10]
bottom_right = [35.50,51.70]

folium.Circle(
    location=[36.228414038516235, 59.64655688111786],
    radius=60000,
    color='blue',
    fill=True,
    fill_color='green'
).add_to(mashhad)

# Display map
mashhad
