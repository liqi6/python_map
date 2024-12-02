import streamlit as st
import leafmap.foliumap as leafmap

m = leafmap.Map(center=[23.5,121], zoom=7, minimap_control=True)
data = "https://raw.githubusercontent.com/liqi6/test/refs/heads/main/COA_OpenData.csv"
m.add_points_from_xy(
  data,
  x="lon",
  y="lat",
  icon_names=["MarketName", "YearMonth", "ClosedDate"],
  spin=True,
)
