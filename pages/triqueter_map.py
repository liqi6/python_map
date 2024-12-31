import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import DualMap
from streamlit_folium import st_folium
import leafmap

# 標題
st.title("歷史種植分佈數據可視化")

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
m = folium.Map(location=[24.4, 120.6], zoom_start=8)
# 定義顏色
colors = {1920: 'firebrick', 1950: 'indianred', 2000: 'lightcoral'}
# 為每一個資料點創建圓形標記
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['緯度'], row['經度']],
        radius=row['種植面積 (公頃)'] / 10,
        color=colors[row['年份']],
        fill=True,
        fill_color=colors[row['年份']],
        fill_opacity=0.6,
        tooltip=f"{row['地區']} ({row['年份']}): {row['種植面積 (公頃)']} 公頃"
    ).add_to(m)

# 在 Streamlit 中顯示 Folium 地圖
st.subheader("各地區不同年份種植面積地圖")
st_folium(m, width=725)
