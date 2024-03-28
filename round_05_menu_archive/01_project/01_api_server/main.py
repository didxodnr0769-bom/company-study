from http import HTTPStatus
from flask import Flask, jsonify, request
from flask_cors import CORS
from util.scrap import request_html
from util.scheduler import start_scheduler
from util.push import send_message
import requests

app = Flask(__name__)
CORS(app)

# 스크랩 타겟 페이지
SCRAP_TARGET = "http://127.0.0.1:5500/02_mock_menu_page"

# PROXY_URL = "http://localhost:3000"
PROXY_URL = "https://dont-go-cat-yang.koyeb.app";

# 스크랩핑 인터벌
SCRAP_INTERVAL_TIME = 10

# 전역 데이터 저장 변수
DATA = []



# 스크랩 시작 함수
def start_scraping():
     global DATA
     result = request_html(SCRAP_TARGET)
     print("데이터를 요청중입니다... ")
     # 데이터가 존재하고, 이전 데이터와 다른 경우에만 데이터 저장 & Push 요청
     if result is not None and DATA != result:
        DATA = result
        # proxy 서버에 토큰 리스트 요청
        tokens = requests.get(PROXY_URL+"/token/list").json()
        print("데이터 변경사항이 있습니다 토큰 : ", tokens)
        # 1. 변경된 데이터 push 요청
        send_message(tokens, "메뉴 업데이트 알림", "메뉴가 업데이트 되었습니다.")
        # 2. 변경된 데이터 서버 저장 요청 ( To. Expree Server )
        regist_menu(result)
        


# 메뉴 등록 요청 ( to express server )
def regist_menu(data):
   response = requests.post(PROXY_URL+"/menu/regist", json={ "menu" : data})




# 주기적 스크랩핑 요청
start_scheduler(start_scraping,SCRAP_INTERVAL_TIME)




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)

