import folium
import pandas
from geopy.geocoders import ArcGIS

def color_producer(name):
    if 'Muthu' in name:
        return 'orange'
    elif 'Kavin' in name:
        return 'purple'
    else:
        return 'blue'

nm = ArcGIS()
n =nm.geocode('115, Nainar Street, Tenkasi, Tirunelveli, Tamil Nadu')
#print(n.latitude, n.longitude)

df = pandas.read_csv('house.txt')
df['Address'] = df['Address']+ ', '+df['City']+', '+df['State']
df['Coordinates'] = df['Address'].apply(nm.geocode)
df['Latitude'] = df['Coordinates'].apply(lambda x:x.latitude)
df['Longitude'] = df['Coordinates'].apply(lambda x:x.longitude)
print(df['Name'])
lat = list(df['Latitude'])
lon = list(df['Longitude'])
name = list(df['Name'])
html = """<h4>Welcome to %s</h4>
"""


map = folium.Map(location=[8.5,77], zoom_start=10, tiles= 'Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')
for lt,ln, n in zip(lat, lon, name):
    iframe = folium.IFrame(html=html % n, width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(n))))
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), fill_color=color_producer(n), color= 'black', fil_opacity=0.7))
map.add_child(fg)
map.save('home_map.html')