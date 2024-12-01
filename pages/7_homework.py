import leafmap

m = leafmap.Map()
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.csv"
m.add_marker_cluster(url, x="longitude", y="latitude", layer_name="World cities")
m
