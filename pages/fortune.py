import os
import random
import streamlit as st
from linebot.models import ImageSendMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
import sqlite3

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

# 模擬產品選單
products = ["藺草帽子"]

# 顯示顏色的描述和圖像
def show_color_info(color_name):
    """顯示顏色對應的資訊"""
    if color_name in colors_data:
        data = colors_data[color_name]
        st.write(f"顏色: {color_name}")
        st.write(f"象徵意義: {data['象徵意義']}")
        st.write(f"感受: {data['感受']}")
        st.write(f"心情: {data['心情']}")
    else:
        st.write("抱歉，這個顏色資料不存在。")

# 顯示產品選單按鈕
def create_product_buttons_template():
    """創建產品選單"""
    button_actions = [URIAction(label=product, uri=f"https://example.com/product/{product}") for product in products]
    buttons_template = TemplateSendMessage(
        alt_text="產品選單",
        template=ButtonsTemplate(
            title="產品選單",
            text="請選擇想了解的產品種類",
            actions=button_actions
        )
    )
    return buttons_template

# 顯示產品選單
def show_product_buttons():
    st.write("請選擇想了解的產品種類:")
    for product in products:
        if st.button(product):
            st.write(f"您選擇了: {product}")

# 主頁面
def main():
    st.title("顏色與產品展示")
    st.write("請選擇顏色以查看相關資料:")

    # 顯示顏色選項按鈕
    color = st.selectbox("顏色選擇", list(colors_data.keys()))
    if st.button("查看顏色資料"):
        show_color_info(color)

    # 顯示產品選單
    if st.button("查看產品選單"):
        show_product_buttons()

if __name__ == "__main__":
    main()
