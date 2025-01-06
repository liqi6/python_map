import os
import random
import streamlit as st


# 當用戶選擇顏色時，顯示該顏色的詳細資料
selected_color = st.selectbox("選擇一個顏色", list(colors_data.keys()))
if selected_color:
    color_info = colors_data[selected_color]
    st.write(f"象徵意義: {color_info['象徵意義']}")
    st.write(f"感受: {color_info['感受']}")
    st.write(f"心情: {color_info['心情']}")
    
