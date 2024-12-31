import streamlit as st
import folium
from folium.plugins import DualMap
from streamlit_folium import st_folium
import geopandas as gpd
import pandas as pd
import leafmap

# 定義資料來源
csv_1950_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/1950.csv"
csv_2000_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/2000.csv"
final_csv_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/final_planting_area.csv"
geojson_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/simplified_townships.geojson"

# 讀取 CSV 和 GeoJSON 資料
st.subheader("讀取資料中...")
try:
    df_1950 = pd.read_csv(csv_1950_url)
    df_2000 = pd.read_csv(csv_2000_url)
    planting_data = pd.read_csv(final_csv_url)
    geojson_data = gpd.read_file(geojson_url)
    st.success("資料讀取成功！")
except Exception as e:
    st.error(f"資料讀取失敗: {e}")
    st.stop()

# 繪製第一張 Folium 地圖
st.subheader("Folium 地圖：1950 年與 2000 年")
try:
    folium_map = folium.Map(location=[23.5, 121], zoom_start=8)
    # 添加 1950 年資料
    for _, row in df_1950.iterrows():
        folium.CircleMarker(
            location=[row["緯度"], row["經度"]],
            radius=3,
            color="green",
            fill=True,
        ).add_to(folium_map)
    # 添加 2000 年資料
    for _, row in df_2000.iterrows():
        folium.CircleMarker(
            location=[row["緯度"], row["經度"]],
            radius=3,
            color="blue",
            fill=True,
        ).add_to(folium_map)

    st_folium(folium_map, width=700, height=500)
except Exception as e:
    st.error(f"Folium 地圖繪製失敗: {e}")

# 繪製雙視圖地圖
st.subheader("DualMap 雙視圖地圖")
try:
    dual_map = DualMap(location=[23.5, 121], zoom_start=8)
    # 左側地圖（1950 年）
    for _, row in df_1950.iterrows():
        folium.CircleMarker(
            location=[row["緯度"], row["經度"]],
            radius=3,
            color="green",
            fill=True,
        ).add_to(dual_map.m1)
    # 右側地圖（2000 年）
    for _, row in df_2000.iterrows():
        folium.CircleMarker(
            location=[row["緯度"], row["經度"]],
            radius=3,
            color="blue",
            fill=True,
        ).add_to(dual_map.m2)

    st_folium(dual_map, width=700, height=500)
except Exception as e:
    st.error(f"DualMap 地圖繪製失敗: {e}")

# 合併 GeoJSON 和種植面積資料
st.subheader("Leafmap 地圖：各地區種植面積")
try:
    geojson_data = geojson_data.merge(
        planting_data, left_on="name", right_on="地區", how="left", suffixes=('_geojson', '_csv')
    )
    geojson_data["種植面積 (公頃)"] = geojson_data["種植面積 (公頃)"].fillna(0)

    # 創建 Leafmap 地圖
    leafmap_map = leafmap.Map(center=[24.406, 120.653], zoom=12)
    leafmap_map.add_data(
        geojson_data,
        column="種植面積 (公頃)",
        cmap="Blues",
        legend_title="種植面積 (公頃)",
    )

    # 在 Streamlit 中顯示地圖
    leafmap_map.to_streamlit()
except Exception as e:
    st.error(f"Leafmap 地圖繪製失敗: {e}")
