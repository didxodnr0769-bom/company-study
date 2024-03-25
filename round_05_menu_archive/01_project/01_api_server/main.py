from http import HTTPStatus
from flask import Flask, jsonify, request
from flask_cors import CORS
from util.scrap import request_html
from util.scheduler import start_scheduler
from util.scrap import get_scrap_data

app = Flask(__name__)
CORS(app)

# 스크랩 타겟 페이지
SCRAP_TARGET = "http://127.0.0.1:5500/02_mock_menu_page/index.html"

# 스크랩핑 인터벌
SCRAP_INTERVAL_TIME = 5

def start_scraping():
     request_html(SCRAP_TARGET)



# 초기 1회 스크랩핑 요천
start_scraping()
# 주기적 스크랩핑 요청
start_scheduler(start_scraping,SCRAP_INTERVAL_TIME)






@app.route('/test/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})



@app.route('/mock/menu/list', methods=['GET'])
def mock_menu_list():
      data =  get_scrap_data()
      return jsonify({'code': '200', 'result': {
        'menu_list': data
      }})



@app.route('/post', methods=['POST'])
def post():
    params = request.get_json()
    print('???')

    result = jsonify({"data": params, "status": HTTPStatus.OK})

    return result




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)

