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
    data = pd.read_csv(csv_url)
    geojson_data = gpd.read_file(geojson_url)
    st.success("資料讀取成功！")
except Exception as e:
    st.error(f"資料讀取失敗: {e}")
    st.stop()

# 合併 GeoJSON 和 CSV
st.subheader("合併 GeoJSON 和 CSV 資料")
try:
    st.write("原始 GeoJSON 資料：")
    st.write(geojson_data.head())
    st.write("原始 CSV 資料：")
    st.write(data.head())

    # 合併資料
    geojson_data = geojson_data.merge(
        data, left_on="name", right_on="地區", how="left", suffixes=('_geojson', '_csv')
    )
    # 填充空值
    geojson_data["種植面積 (公頃)"] = geojson_data["種植面積 (公頃)"].fillna(0)
    st.write("合併後的 GeoDataFrame：")
    st.write(geojson_data.head())
except Exception as e:
    st.error(f"合併資料失敗: {e}")
    st.stop()

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

   st.subheader("各地區不同年代種植面積")
try:
    leafmap_map = leafmap.Map(center=[23.5, 121], zoom=8)
    leafmap_map.add_data(
        geojson_data,
        column="種植面積 (公頃)",
        cmap="Blues",
        legend_title="種植面積 (公頃)",
    )
    leafmap_map.to_streamlit()
except Exception as e:
    st.error(f"Leafmap 地圖繪製失敗: {e}")

# 讀取資料
st.subheader("讀取資料中...")
try:
    data_1950 = pd.read_csv(csv_1950_url)
    geojson_data = gpd.read_file(geojson_url)
    st.success("資料讀取成功！")
except Exception as e:
    st.error(f"資料讀取失敗: {e}")
    st.stop()

# 篩選 1950 年的資料
st.subheader("處理資料中...")
try:
    data_1950_filtered = data_1950[data_1950["年份"] == 1950]
    # 合併 GeoJSON 與 1950 年資料
    geojson_data = geojson_data.merge(
        data_1950_filtered, left_on="name", right_on="地區", how="left", suffixes=('_geojson', '_csv')
    )
    # 填充空值為 0
    geojson_data["種植面積 (公頃)"] = geojson_data["種植面積 (公頃)"].fillna(0)
    st.write("合併後的 GeoDataFrame：")
    st.write(geojson_data.head())
except Exception as e:
    st.error(f"資料處理失敗: {e}")
    st.stop()

# 繪製 1950 年的面量圖
st.subheader("1950 年各地區種植面積面量圖")
try:
    data_1950 = data[data["年份"] == 1950]
    geojson_data_1950 = geojson_data.merge(
        data_1950, left_on="name", right_on="地區", how="left", suffixes=('_geojson', '_csv')
    )
    geojson_data_1950["種植面積 (公頃)"] = geojson_data_1950["種植面積 (公頃)"].fillna(0)

    leafmap_map_1950 = leafmap.Map(center=[23.5, 121], zoom=8)
    leafmap_map_1950.add_data(
        geojson_data_1950,
        column="種植面積 (公頃)",
        cmap="YlGnBu",
        legend_title="1950 年種植面積 (公頃)",
    )
    leafmap_map_1950.to_streamlit()
except Exception as e:
    st.error(f"1950 年地圖繪製失敗: {e}")

