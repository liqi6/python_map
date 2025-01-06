import requests
import streamlit as st

# API 授權碼與基本 URL
API_KEY = "CWA-625AF5AD-842B-4BF9-9340-A8DB15077F9D"
BASE_URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

def normalize_city_name(city):
    """將輸入的城市名稱中的'台'替換為'臺'"""
    return city.replace("台", "臺")

def fetch_weather_data(city):
    """從 API 獲取天氣資料"""
    params = {
        "Authorization": API_KEY,
        "locationName": city,
        "format": "JSON",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise ValueError("找不到指定地名的天氣資料")
    else:
        raise Exception(f"HTTP 錯誤：{response.status_code}")

def parse_weather_data(data, city):
    """解析天氣資料並格式化輸出"""
    try:
        location_data = data["records"]["location"][0]
        weather_elements = location_data["weatherElement"]

        forecast = []
        for i in range(len(weather_elements[0]["time"])):
            start_time = weather_elements[0]["time"][i]["startTime"]
            end_time = weather_elements[0]["time"][i]["endTime"]
            description = weather_elements[0]["time"][i]["parameter"]["parameterName"]
            min_temp = weather_elements[1]["time"][i]["parameter"]["parameterName"]
            max_temp = weather_elements[2]["time"][i]["parameter"]["parameterName"]
            rain_prob = weather_elements[4]["time"][i]["parameter"]["parameterName"]

            forecast.append(
                f"{start_time} ~ {end_time}:\n"
                f"  天氣：{description}\n"
                f"  氣溫：{min_temp}°C ~ {max_temp}°C\n"
                f"  降雨機率：{rain_prob}%"
            )

        return f"{city}未來天氣預報：\n" + "\n\n".join(forecast)
    except (KeyError, IndexError):
        raise ValueError("資料解析失敗，可能是輸入錯誤或資料缺失")

def get_weekly_weather(city):
    """獲取並顯示天氣預報"""
    city = normalize_city_name(city)
    try:
        data = fetch_weather_data(city)
        return parse_weather_data(data, city)
    except ValueError as ve:
        return f"輸入錯誤：{ve}"
    except Exception as e:
        return f"系統錯誤：{e}"

# Streamlit 主程式
st.title("臺灣天氣預報查詢")
city_name = st.text_input("輸入城市名稱（例如：台北市或臺北市）：", "")

if city_name.strip():
    result = get_weekly_weather(city_name)
    st.write(result)
