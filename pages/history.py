import requests
from bs4 import BeautifulSoup

def fetch_static_content(url, class_name):
    """
    使用 requests 和 BeautifulSoup 爬取靜態內容
    - url: 目標網站的 URL
    - class_name: 目標元素的類名
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 確保成功響應
    except requests.exceptions.RequestException as e:
        print(f"無法請求網址 {url}，錯誤原因：{e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(class_=class_name)

    results = []
    seen_items = set()  # 去重處理
    for el in elements:
        title = el.get_text(strip=True)
        link = el.get('href')
        if title and link and (title, link) not in seen_items:
            results.append((title, link))
            seen_items.add((title, link))
    return results

def main():
    # 定義要爬取的網站資料
    sites = [
        {
            "url": "https://nchdb.boch.gov.tw/search?query=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2",
            "class_name": "gs-title",  # 根據網站實際情況調整
        },
        {
            "url": "https://www.sunnyrush.com/search/index-1.asp?parser=99,9,18&q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2#gsc.tab=0&gsc.q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2&gsc.page=1",
            "class_name": "gs-title",  # 根據網站實際情況調整
        },
    ]

    all_results = []
    for site in sites:
        results = fetch_static_content(site["url"], site["class_name"])
        all_results.extend(results)

    # 輸出爬取結果
    for title, link in all_results:
        print(f"標題: {title}")
        print(f"連結: {link}")

if __name__ == "__main__":
    main()
