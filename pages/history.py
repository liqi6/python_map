import requests
from bs4 import BeautifulSoup
import streamlit as st

def fetch_static_content(url, class_name):
    """從靜態網站中抓取內容"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"無法請求網址 {url}，錯誤原因：{e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(class_=class_name)
    return [(el.get_text(strip=True), el.get('href')) for el in elements]

def main():
    st.title("歷史資料爬取工具")
    
    sites = [
        {"url": "https://nchdb.boch.gov.tw/search?query=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2", "class_name": "gs-title"},
        {"url": "https://www.sunnyrush.com/search/index-1.asp?parser=99,9,18&q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2#gsc.tab=0&gsc.q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2&gsc.page=1", "class_name": "gs-title"},
    ]

    for site in sites:
        st.header(f"爬取自 {site['url']}")
        results = fetch_static_content(site["url"], site["class_name"])
        for title, link in results:
            st.write(f"- [{title}]({link})")

if __name__ == "__main__":
    main()
