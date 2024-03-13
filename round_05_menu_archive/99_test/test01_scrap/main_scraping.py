import schedule
import time

import requests
from bs4 import BeautifulSoup

# url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
url = 'http://127.0.0.1:5500/round_05_menu_archive/00_mock_menu_page/index.html'
response = requests.get(url)

def request_html():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_ul = soup.select_one('#s_content > div.section > ul')
        titles = tag_ul.select('li > dl > dt > a')
        for title in titles:
            print(title.text)
    else : 
        print(response.status_code)


schedule.every(5).seconds.do(request_html)

while True:
    schedule.run_pending()
    time.sleep(1)

