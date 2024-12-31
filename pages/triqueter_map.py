import streamlit as st
import geopandas as gpd
import pandas as pd
import leafmap

# 定義資料來源
csv_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/final_planting_area.csv"
geojson_url = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/simplified_townships.geojson"

# 讀取資料
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

# 繪製 Leafmap 地圖：各地區種植面積
st.subheader("Leafmap 地圖：各地區種植面積")
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

# 篩選 1950 年資料
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

