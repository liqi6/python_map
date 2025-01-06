from requirements import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def scrape_site(driver, url, class_name, wait_time=10):
    """
    通用的網站爬取函數
    - driver: Selenium WebDriver實例
    - url: 目標網站的URL
    - class_name: 目標元素的類名
    - wait_time: 等待元素加載的時間（秒）
    """
    driver.get(url)
    seen_items = set()  # 儲存去重的結果
    results = []

    try:
        # 等待目標元素加載
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        articles = driver.find_elements(By.CLASS_NAME, class_name)

        # 提取標題和連結
        for article in articles:
            title = article.text.strip()
            link = article.get_attribute('href')
            if title and link and (title, link) not in seen_items:
                results.append((title, link))
                seen_items.add((title, link))
    except TimeoutException:
        print(f"未找到符合條件的元素: {url}")

    return results

def main():
    # 設置Chrome選項
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 不顯示瀏覽器視窗
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 啟動瀏覽器
    driver = webdriver.Chrome(options=options)

    # 定義要爬取的網站資料
    sites = [
        {
            "url": "https://nchdb.boch.gov.tw/search?query=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2",
            "class_name": "gs-title",
        },
        {
            "url": "https://www.sunnyrush.com/search/index-1.asp?parser=99,9,18&q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2#gsc.tab=0&gsc.q=%E8%97%BA%E8%8D%89%E6%AD%B7%E5%8F%B2&gsc.page=1",
            "class_name": "gs-title",
        },
    ]

    # 爬取所有網站資料
    all_results = []
    for site in sites:
        results = scrape_site(driver, site["url"], site["class_name"])
        all_results.extend(results)

    # 關閉瀏覽器
    driver.quit()

    # 輸出所有結果
    for title, link in all_results:
        print(f'標題: {title}')
        print(f'連結: {link}')

if __name__ == "__main__":
    main()
