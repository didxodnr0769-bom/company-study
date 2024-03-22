from http import HTTPStatus
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/test/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/mock/menu/list', methods=['GET'])
def mock_menu_list():
      print("mock_menu_list 요청")
      return jsonify({'code': '200', 'result': {
        'menu_list': [
            {
                'title': 'menu1',
                'menus' : 'menu1\nmenu2\nmenu3',
                'post_url': "https://pf.kakao.com/_Vcbxgb/104567139"
            },            {
                'title': 'menu2',
                'menus' : 'menu1\nmenu2\nmenu3',
                'post_url': "https://pf.kakao.com/_Vcbxgb/104567139"
            },
            {
                'title': 'menu3',
                'menus' : 'menu1\nmenu2\nmenu3',
                'post_url': "https://pf.kakao.com/_Vcbxgb/104567139"
            },
            {
                'title': 'menu4',
                'menus' : 'menu1\nmenu2\nmenu3',
                'post_url': "https://pf.kakao.com/_Vcbxgb/104567139"
            },
        ]
      }})



@app.route('/post', methods=['POST'])
def post():
    params = request.get_json()
    print('???')

    result = jsonify({"data": params, "status": HTTPStatus.OK})

    return result


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)