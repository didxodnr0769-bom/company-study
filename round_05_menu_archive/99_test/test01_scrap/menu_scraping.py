import schedule
import time

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/round_05_menu_archive/00_mock_menu_page/index.html'
response = requests.get(url)

def request_html():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.select_one('#mArticle > div')
        posts = container.select('div')
        print(posts)

        # 아이템 내용 추출 
        for post in posts:
            title = post.select_one('.post_txt > .tit_post')
            print(title)

        # titles = tag_ul.select('li > dl > dt > a')
        # for title in titles:
        #     print(title.text)
    else : 
        print(response.status_code)



request_html()

# schedule.every(5).seconds.do(request_html)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

