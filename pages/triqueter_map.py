import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import DualMap
from streamlit_folium import st_folium
import leafmap

# 標題
st.title("藺草種植分佈地圖")

@st.cache_data
def load_data():
    """讀取遠端數據並快取以加速應用執行"""
    csv_url_1950 = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/1950.csv"
    csv_url_2000 = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/2000.csv"
    geojson_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/simplified_townships.geojson"
    planting_data_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/final_planting_area.csv"
    
    df_1950 = pd.read_csv(csv_url_1950)
    df_2000 = pd.read_csv(csv_url_2000)
    geojson_data = gpd.read_file(geojson_url)
    planting_data = pd.read_csv(planting_data_url)
    return df_1950, df_2000, geojson_data, planting_data

df_1950, df_2000, geojson_data, planting_data = load_data()

# Folium 雙視圖地圖
st.subheader("1950 與 2000 年種植分佈")
m = DualMap(location=[23.5, 121], zoom_start=8)

for _, row in df_1950.iterrows():
    folium.CircleMarker(
        location=[row['緯度'], row['經度']],
        radius=3,
        color='green',
        fill=True,
    ).add_to(m.m1)

for _, row in df_2000.iterrows():
    folium.CircleMarker(
        location=[row['緯度'], row['經度']],
        radius=3,
        color='blue',
        fill=True,
    ).add_to(m.m2)

# 在 Streamlit 中顯示地圖
st_folium(m, width=800)

# Leafmap 地圖視覺化
st.subheader("各地區種植面積")
geojson_data = geojson_data.merge(
    planting_data, left_on="name", right_on="地區", how="left", suffixes=('_geojson', '_csv')
)
leafmap_map = leafmap.Map(center=[24.406, 120.653], zoom=12)
leafmap_map.add_data(geojson_data, column="種植面積 (公頃)", cmap="Blues", legend_title="種植面積 (公頃)")

# 使用 Leafmap 在 Streamlit 中顯示地圖
leafmap_map.to_streamlit()

