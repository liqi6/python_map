import os
import streamlit as st

# 設定圖片存放路徑
IMAGE_PATH = "static/colours"  # 資料夾路徑

# 顯示所有顏色
st.title("產品顏色列表")

# 顯示顏色資料
for color, info in colors_data.items():
    st.subheader(color)  # 顯示顏色名稱
    st.write(f"象徵意義: {info['象徵意義']}")
    st.write(f"感受: {info['感受']}")
    st.write(f"心情: {info['心情']}")
    
    # 根據顏色名稱尋找圖片並顯示
    image_filename = f"{color}.jpg"  # 假設圖片是以顏色名稱命名的
    image_path = os.path.join(IMAGE_PATH, image_filename)
    
    if os.path.exists(image_path):  # 檢查圖片是否存在
        st.image(image_path, caption=color, use_column_width=True)  # 顯示圖片
    else:
        st.write("此顏色沒有圖片")

# 當用戶選擇顏色時，顯示該顏色的詳細資料
selected_color = st.selectbox("選擇一個顏色", list(colors_data.keys()))
if selected_color:
    color_info = colors_data[selected_color]
    st.write(f"象徵意義: {color_info['象徵意義']}")
    st.write(f"感受: {color_info['感受']}")
    st.write(f"心情: {color_info['心情']}")
    
    # 顯示顏色圖片
    image_filename = f"{selected_color}.jpg"  # 根據選擇的顏色查找圖片
    image_path = os.path.join(IMAGE_PATH, image_filename)
    
    if os.path.exists(image_path):  # 檢查圖片是否存在
        st.image(image_path, caption=selected_color, use_column_width=True)  # 顯示圖片
    else:
        st.write("此顏色沒有圖片")
