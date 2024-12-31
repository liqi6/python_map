!pip install -U leafmap
!pip install fiona
!pip install folium branca
!pip install requests geopandas
!pip install geopandas leafmap pandas
!pip install mapclassify
import geopandas as gpd
import leafmap
import pandas as pd
import folium

data=pd.read_csv('https://raw.githubusercontent.com/liqi6/test/refs/heads/main/%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2%E5%88%86%E5%B8%83%E6%95%B8%E6%93%9A.csv')
data.head()

m = folium.Map(location=[24.4, 120.6], zoom_start=8)

colors = {1920: 'firebrick', 1950: 'indianred', 2000: 'lightcoral'}

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
m
