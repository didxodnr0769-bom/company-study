# scrap을 위한 함수들을 정의한 파일입니다.
import requests
from bs4 import BeautifulSoup
from datetime import datetime

DATA = []



def request_html(url):
    global DATA
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
            img = post.select_one("a.link_post > div > img").get("src")
            
            menus = "테스트\n메뉴입니다\n아직 OCR 미구현이라"

            result.append({
                "title" : content.text,
                "menus" : menus,
                "post_url" : post_url
            })


        
        
        # 이전 저장 데이터와 비교하여 분기처리
        # 1. 이전 데이터와 다른 경우
        #  - 데이터 저장
        #  - push 요청
        if(DATA != result) : 
            DATA = result
            print("time : " , datetime.now() )
            print("DATA : " , DATA)
            print("result : " , result)
            print("DATA == result" , DATA==result)
            print("----------------------------------------------")
            
    else : 
        print(response.status_code)

def get_scrap_data(): 
    return DATA

