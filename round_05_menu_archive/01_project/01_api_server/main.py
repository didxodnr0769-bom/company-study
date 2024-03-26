from http import HTTPStatus
from flask import Flask, jsonify, request
from flask_cors import CORS
from util.scrap import request_html
from util.scheduler import start_scheduler
from util.push import send_message

app = Flask(__name__)
CORS(app)

# 스크랩 타겟 페이지
SCRAP_TARGET = "http://127.0.0.1:5500/02_mock_menu_page/index.html"

PROXY_URL = "http://localhost:3000"

# 스크랩핑 인터벌
SCRAP_INTERVAL_TIME = 5

# 전역 데이터 저장 변수
DATA = []

# push용 사용자 토큰 리스트
USER_TOKENS = []


# 스크랩 시작 함수
def start_scraping():
     global DATA
     result = request_html(SCRAP_TARGET)
     print("데이터를 요청중입니다... USER : ", USER_TOKENS)
     # 데이터가 존재하고, 이전 데이터와 다른 경우에만 데이터 저장 & Push 요청
     if result is not None and DATA != result:
        DATA = result
        # proxy 서버에 토큰 리스트 요청
        tokens = requests.get(PROXY_URL+"/token/list").json()
        send_message(tokens, "메뉴 업데이트 알림", "메뉴가 업데이트 되었습니다.")



# 주기적 스크랩핑 요청
start_scheduler(start_scraping,SCRAP_INTERVAL_TIME)



# 토큰 저장 API
# 사용자 토큰을 받아서 전역 변수에 저장
@app.route('/token/regist', methods=['POST'])
def post():
    print('token/regist')
    params = request.get_json()
    global USER_TOKENS
    new_token = params['token']
    # 중복 토큰 체크
    if new_token not in USER_TOKENS:
        USER_TOKENS.append(new_token)
    result = jsonify({"data": "", "status": HTTPStatus.OK})

    return result





@app.route('/menu/list', methods=['GET'])
def mock_menu_list():
      global DATA
      return jsonify({'code': '200', 'result': {
        'menu_list': DATA
      }})






if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)

