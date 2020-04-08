import folium
import pandas as pd

# importing the datasets 
df = pd.read_csv("volcanoes.csv", encoding="ISO-8859-1")
ports = pd.read_csv("ports.csv")
mountains = pd.read_csv("mountains.csv", encoding="ISO-8859-1")
ski = pd.read_csv("skicenters.csv", encoding="ISO-8859-1")
lakes = pd.read_csv("lakes.csv", encoding="ISO-8859-1", sep='!')

# data for volcanoes
df = df.loc[df["LOCATION"] == "Greece"]
latitude = list(df["LATITUDE"])
longitude = list(df["LONGITUDE"])
name = list(df["NAME"])
elevation = list(df["ELEV"])

# port data
pname = list(ports["Name"])
platitude = list(ports["Latitude"])
plongitude = list(ports["Longitude"])

# mountains data
mname = list(mountains["Name"])
melevation = list(mountains["Elevation"])
mlatitude = list(mountains["Latitude"])
mlongitude = list(mountains["Longitude"])

# ski centers data
sname = list(ski["Name"])
slatitude = list(ski["Latitude"])
slongitude = list(ski["Longitude"])

# lakes data
lname = list(lakes["Name"])
llatitude = list(lakes["Latitude"])
llongitude = list(lakes["Longitude"])
lsurface = list(lakes["Surface area"])

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
                               icon_color="white", icon="fire", prefix="fa")))

# create feauture group for ports
fgp = folium.FeatureGroup(name="Ports")

for lat, lon, nm in zip(platitude, plongitude, pname):
    fgp.add_child(folium.Marker(
            location = [lat, lon],
            popup = nm + " port.",
            icon = folium.Icon(icon="anchor", prefix="fa")))

# create feauture group for mountains
fgm = folium.FeatureGroup(name="Mountains")

for lat, lon, nm, elev in zip(mlatitude, mlongitude, mname, melevation):
    fgm.add_child(folium.CircleMarker(
            location = [lat, lon],
            radius = 8,
            popup = nm + " has " + str(elev) + " of elevation.",
            fill_color="#A52A2A",
            color = "#800000",
            fill_opacity = 0.7))

# create feauture group for ski resorts
fgs = folium.FeatureGroup(name="Ski resorts")

for lat, lon, nm in zip(slatitude, slongitude, sname):
    fgs.add_child(folium.Marker(
            location = [lat, lon],
            popup = nm,
            icon = folium.Icon(icon="thumb-tack", prefix="fa", color="lightgray", icon_color="white")))

# create feauture group for lakes
fgl = folium.FeatureGroup(name="Lakes")

for lat, lon, nm, sa in zip(llatitude, llongitude, lname, lsurface):
    fgl.add_child(folium.Marker(
            location = [lat, lon],
            popup = "The surface area of " +nm+" is "+sa,
            icon = folium.Icon(icon="tint", prefix="fa", color="darkblue", icon_color="white")))
    
map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgm)
map.add_child(fgs)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Greece.html")