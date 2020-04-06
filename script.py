import folium
import pandas as pd

# importing the dataset as a csv file, 
df = pd.read_csv("volcanoes.csv", encoding="ISO-8859-1")

# and taking only the data for Greece
df = df.loc[df["LOCATION"] == "Greece"]
latitude = list(df["LATITUDE"])
longitude = list(df["LONGITUDE"])
name = list(df["NAME"])
elevation = list(df["ELEV"])

# Function to change the marker color  
# according to the elevation of volcano 
def color_producer(elev):
    if elev in range(0,300):
        color = "green"
    elif elev in range(301,600):
        color = "orange"
    else:
        color = "red"
    return color

# create the map
map = folium.Map(
        location = [39.0742, 21.8243], #Greece's Coordinates
        zoom_start = 6,
        tiles = "Stamen Terrain"
        )

# create feauture group for volcanoes
fgv= folium.FeatureGroup(name="Volcanoes")

for lat, lon, nm, elev in zip(latitude, longitude, name, elevation):
    fgv.add_child(folium.Marker(
            location = [lat, lon],
            popup = nm + " has " + str(elev) + " m of elevation.",
            icon = folium.Icon(color = color_producer(elev),
                               icon_color="white", icon="check")))
    



map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Greece.html")      