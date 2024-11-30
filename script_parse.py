from bs4 import BeautifulSoup
import requests 
import json
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


def get_main_subject(item_data):
    """
    取得主題
    """
    print("當前處理文章 ", item_data['title'])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = item_data['href']
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_title = soup.find('h3', class_='ir-article__topic').find('a')
        article_title_href = article_title['href']
        article_title_text = article_title.text.strip()
        return {
            "title": article_title_text,
            "href": article_title_href,
            "child":[item_data]
        }
def already_exist(result, main_subject_json):
    """
    檢查是否已經存在
    """
    for item in result:
        if item['href'] == main_subject_json['href']:
            return True
    return False

if __name__ == "__main__":
    with open('result.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    result = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(get_main_subject, item_data) for item_data in json_data]
        for future in concurrent.futures.as_completed(futures):
            try:
                main_subject_json = future.result()
                if main_subject_json and not already_exist(result, main_subject_json):
                    result.append(main_subject_json)
                elif main_subject_json and already_exist(result, main_subject_json):
                    for item in result:
                        if item['href'] == main_subject_json['href']:
                            item['child'].append(main_subject_json['child'][0])
            except Exception as e:
                print(f"發生錯誤: {e}")
    with open('result_main_subject.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
