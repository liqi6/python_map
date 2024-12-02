import streamlit as st
import leafmap.foliumap as leafmap

m = leafmap.Map(center=[23.5,121], zoom=7, minimap_control=True)
data = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/C-B0074-001?Authorization=rdec-key-123-45678-011121314"
m.add_points_from_xy(
  data,
  x="StationLongitude",
  y="StationLatitude",
  icon_names=["StationName", "status", "CountyName","Location"],
  spin=True,
    )
m.to_streamlit(height=500)
