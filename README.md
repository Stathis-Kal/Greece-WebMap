# Greece-WebMap 🗺

## Info
This repository contains a Python script which generates via Folium library an interactive WebMAP of Greece.  

I used some sample data to demonstrate
- Volcanoes 📌
- Ports 📌
- Mountains 📌
- Ski resorts 📌
- Lakes 📌

across the Greece.

The points on the map are **interactive** and you can click on them to display some valuable information.

The color of Volcanoes marker is defined via the following function.
Basically the higher the elevation of a volcano is, the darker the color becames.

```python
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
  ```

There is also a layer control, in which you can choose what do you want to be displayed on the map.
The layer control is located top right on your screen.

[![CodeFactor](https://www.codefactor.io/repository/github/stathis-kal/greece-webmap/badge/master)](https://www.codefactor.io/repository/github/stathis-kal/greece-webmap/overview/master)

Licensed under [MIT License.](LICENSE)
