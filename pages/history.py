import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_static_content(url, class_name):
    """從靜態網站中抓取內容"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all(class_=class_name)
        
        results = []
        for el in elements:
            title = el.get_text(strip=True)
            link = el.get("href")
            # 確保連結為完整的URL
            if link and not link.startswith('http'):
                link = f'https://www.sunnyrush.com{link}'  # 根據需要修改為正確的基礎 URL
            if title and link:
                results.append((title, link))
        return results
    except requests.exceptions.RequestException as e:
        st.error(f"無法請求網址 {url}，錯誤原因：{e}")
        return []

def display_site_results(header, url, class_name):
    """顯示單個網站的爬取結果"""
    st.header(header)
    results = fetch_static_content(url, class_name)
    if results:
        for title, link in results:
            st.write(f"[{title}]({link})")
    else:
        st.write("未找到相關結果，請檢查網址或網站內容。")

def main():
    """主程式入口"""
    # 第一個網站 - 國家文化資產網
    display_site_results(
        header="國家文化資產網",
        url="https://nchdb.boch.gov.tw/search?query=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2",
        class_name="gs-title",
    )

    # 第二個網站 - SunnyRush 藺子
    display_site_results(
        header="藺子",
        url="https://www.sunnyrush.com/search/index-1.asp?parser=99,9,18&q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2#gsc.tab=0&gsc.q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2&gsc.page=1",
        class_name="gs-title",
    )

# Streamlit 主執行邏輯
if __name__ == "__main__":
    main()
