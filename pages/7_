m = leafmap.Map(center=[24, 124], zoom=4)
people = "https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-000605-071"
regions = "https://maps.nlsc.gov.tw/download/CH_3857_Contour_OpenData.zip"

m.add_geojson(regions, layer_name="US Regions")
m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    color_column="region",
    icon_names=["gear", "map", "leaf", "globe"],
    spin=True,
    add_legend=True,
)
