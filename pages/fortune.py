import sqlite3
import os
from flask import Flask, request, jsonify, g, render_template

# 初始化Flask應用程式
app = Flask(__name__)

# 設定圖片存放路徑
IMAGE_PATH = "static/colours"

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

# 產品種類
products = ["藺草帽子"]

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect('color_product.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def get_image_url(color_name):
    """根據顏色名稱返回對應的圖片URL"""
    filename = f"{color_name}.jpg"  # 假設圖片命名為"顏色名稱.jpg"
    file_path = os.path.join(IMAGE_PATH, filename)
    if os.path.exists(file_path):
        return url_for('static', filename=f"colours/{filename}", _external=True)
    else:
        return None  # 若圖片不存在則返回None

@app.route("/")
def index():
    # 顯示產品顏色和相關資訊
    return render_template("index.html", colors=colors_data)

@app.route("/product/<color_name>")
def product_details(color_name):
    # 顯示特定顏色的詳細資料
    color_info = colors_data.get(color_name)
    if color_info:
        image_url = get_image_url(color_name)
        return render_template("product_details.html", color=color_name, info=color_info, image_url=image_url)
    else:
        return "產品資訊未找到", 404

if __name__ == "__main__":
    app.run(debug=True)
