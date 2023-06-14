import folium

mashhad = folium.Map(location=[36.29633610452868, 59.61219276319479], zoom_start=11)
folium.Marker(location=[36.228414038516235, 59.64655688111786], popup='Airport', icon=folium.Icon(icon='plane', prefix='fa')).add_to(mashhad)

top_left = [36.37392118145343, 59.47255917108464]
bottom_right = [36.31307101925791, 59.545240245952236]

rect2 = folium.Rectangle(
    bounds=[top_left, bottom_right],
    fill=True,
    fill_color='red',
    color='blue',
    opacity=0.5,
    fill_opacity=0.2
).add_to(mashhad)

mashhad
