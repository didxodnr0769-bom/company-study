# scrap을 위한 함수들을 정의한 파일입니다.
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .ocr import request_extract




def request_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.select_one('#mArticle > div')
        posts = container.select('div.wrap_post')
        result = []

        # 아이템 내용 추출 
        for post in posts:
            # 내용 추출 
            # 내용 .post_txt > .tit_post
            content = post.select_one(".post_txt > .tit_post")
            # 해당 원문 게시글 상세 URL
            post_url = post.select_one(".post_profile > .wrap_info > .txt_time > a").get("href")
            # 이미지 경로 a.link_post > div > img
            img = "https:"+post.select_one("a.link_post > div > img").get("src")
            file_name = content.text.replace(" ","_") +".ignore"+ '.jpeg'

            menus_extract = request_extract(img,file_name)


            result.append({
                "title" : content.text,
                "menus" : menus_extract,
                "post_url" : post_url
            })
        return result
            
    else : 
        print(response.status_code)

