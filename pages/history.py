import requests
from bs4 import BeautifulSoup

def fetch_static_content(url, class_name):
    """從靜態網站中抓取內容"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 確保成功響應
    except requests.exceptions.RequestException as e:
        print(f"無法請求網址 {url}，錯誤原因：{e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(class_=class_name)
    
    results = []
    seen_items = set()  # 避免重複結果
    for el in elements:
        title = el.get_text(strip=True)
        link = el.get('href')
        if title and link and (title, link) not in seen_items:
            results.append((title, link))
            seen_items.add((title, link))
    return results

def save_to_file(filename, content):
    """將爬取結果儲存到文字檔"""
    with open(filename, "w", encoding="utf-8") as file:
        for title, link in content:
            file.write(f"{title}\n{link}\n\n")
    print(f"結果已儲存到 {filename}")

def main():
    # 定義要爬取的網站資料
    sites = [
        {"url": "https://nchdb.boch.gov.tw/search?query=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2", "class_name": "gs-title"},
        {"url": "https://www.sunnyrush.com/search/index-1.asp?parser=99,9,18&q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2#gsc.tab=0&gsc.q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2&gsc.page=1", "class_name": "gs-title"},
    ]

    all_results = []
    for site in sites:
        results = fetch_static_content(site["url"], site["class_name"])
        all_results.extend(results)

    if all_results:
        save_to_file("results.txt", all_results)
    else:
        print("沒有抓取到任何結果。")

if __name__ == "__main__":
    main()
