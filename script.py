from bs4 import BeautifulSoup
import requests 
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import json

include_keyword = ['java','spring']
exclude_keyword = ['javascript']
# exclude_keyword = []

def find_java_articles(html_content):
    """
    找出所有java文章
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    # 找出所有的文章區塊
    articles = soup.find_all('div', class_='articles-box')
    for article in articles:
        # 找出文章內容
        txt_div = article.find('div', class_='articles-txt')
        if txt_div and any(keyword.lower() in txt_div.text.lower() for keyword in include_keyword) and not any(keyword.lower() in txt_div.text.lower() for keyword in exclude_keyword):
            # 找出文章標題與url
            title_div = article.find('div', class_='articles-title')
            if title_div:
                title = title_div.find('a').text.strip()
                href = title_div.find('a')['href']
                return {
                    "title": title,
                    "href": href
                }

def get_last_page(html_content):
    """
    取得最後一頁
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    # 找到分頁容器
    pagination = soup.find('nav', class_='pagination-container')
    # 找到所有分頁連結
    page_links = pagination.find_all('a')
    # 取得最後一個有數字的連結的文字
    last_page = None
    for link in page_links:
        if link.text.strip().isdigit():
            last_page = int(link.text.strip())
    return last_page

def search_url(url):
    """
    搜尋文章
    """
    page = url.split('page=')[1]
    print("當前搜尋頁數 ", page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML
        search_result = find_java_articles(response.text)
        if search_result is not None:
            return search_result
    else:
        print("請求失敗",response.status_code)

if __name__ == '__main__':
    # pip install -r requirements.txt
    url = "https://ithelp.ithome.com.tw/2024ironman/contest?tab=latest&page=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        last_page = get_last_page(response.text)
    # last_page = get_last_page(html_content)
    base_url = "https://ithelp.ithome.com.tw/2024ironman/contest?tab=latest&page="
    result = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        urls = [base_url + str(i) for i in range(1, last_page + 1)]
        futures = [executor.submit(search_url, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            try:
                future_result = future.result()
                if future_result is not None:
                    result.append(future_result)
            except Exception as e:
                print(f"發生錯誤: {e}")
    
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
