import os
import random
import streamlit as st

# 顏色列表
colors = ["紅色", "橙色", "黃色", "綠色", "藍色", "紫色", "粉紅色", "黑色", "白色", "灰色", "水藍色"]

# 隨機選擇一個顏色
selected_color = random.choice(colors)

# 顏色與特性
colors_data = {
    "紅色": {"象徵意義": "能量、熱情、行動力", "感受": "熱情、興奮、力量", "心情": "激昂、自信、勇敢"},
    "橙色": {"象徵意義": "活力、創意、友善", "感受": "活潑、溫暖、親切", "心情": "積極、樂觀、朝氣"},
    "黃色": {"象徵意義": "智慧、快樂、啟發", "感受": "明亮、溫暖、希望", "心情": "愉悅、啟發、樂觀"},
    "綠色": {"象徵意義": "平靜、健康、成長", "感受": "清新、放鬆、安全", "心情": "舒心、穩定、安靜"},
    "藍色": {"象徵意義": "冷靜、穩定、信任", "感受": "平靜、智慧、深邃", "心情": "自省、安定、理性"},
    "紫色": {"象徵意義": "靈感、高貴、神秘", "感受": "高雅、啟發、浪漫", "心情": "沉思、靈感、夢幻"},
    "粉紅色": {"象徵意義": "愛情、同情、幸福", "感受": "柔情、甜美、浪漫", "心情": "溫暖、愛意、幸福"},
    "黑色": {"象徵意義": "權力、神秘、蛻變", "感受": "冷靜、內省、謹慎", "心情": "冷靜、內省、謹慎"},
    "白色": {"象徵意義": "純潔、新生、希望", "感受": "清新、純淨、輕鬆", "心情": "開放、安寧、平和"},
    "灰色": {"象徵意義": "中立、平衡、智慧", "感受": "中性、沉穩、現代", "心情": "冷靜、理性、穩重"},
    "水藍色": {"象徵意義": "自由、清新、希望", "感受": "清涼、純粹、輕快", "心情": "自由、舒適、放鬆"},
}

# 顯示標題
st.title("今天的幸運色")

# 顯示隨機選擇的顏色
st.write(f"今天的隨機選擇顏色是: **{selected_color}**")

# 顯示顏色的詳細資料
if selected_color:
    color_info = colors_data[selected_color]
    st.write(f"象徵意義: {color_info['象徵意義']}")
    st.write(f"感受: {color_info['感受']}")
    st.write(f"心情: {color_info['心情']}")
    
# 設定圖片存放路徑 (Google Drive 共享鏈接)
IMAGE_PATH = "https://drive.google.com/uc?export=view&id="

image_id_mapping = {
        "紅色": "1aoGX1vuLopNQLPsUq6Bagkarcmjf5zTf",
        "橙色": "11bcmgVNMjBDvizKi_U1K-5VJjX9HpBXt",
        "黃色": "1SqWhHnkVJGyyJgKyqkGdkWLcrNiWHByf",
        "綠色": "1ulK6MW-NMgpDVwuZDuEXuUjvA4s0zzGo",
        "藍色": "1BJXRXzlebqIc8eRQYLvjdJ8K6c4-Atqj",
        "紫色": "1MaFxsTFUUimdroXkkxyC3RA4XIy1kRD6",
        "粉紅色": "1ObbFyZDFRFIruoO-p-hPBXJf9YHTcftH",
        "白色": "1hG4ER-luuGj1u258l3oc5HgaUa2DPGIk",
        "灰色": "1aoGX1vuLopNQLPsUq6Bagkarcmjf5zTf",
        "水藍色": "1Ao242yXPr-DXqhQKZE4zcmQ6YYFWhsw2",
    }

    # 根據顏色名稱獲取圖片ID
    image_url = f"{IMAGE_PATH}{image_id_mapping[selected_color]}"

    # 顯示圖片
    st.image(image_url, caption=selected_color, use_column_width=True)
