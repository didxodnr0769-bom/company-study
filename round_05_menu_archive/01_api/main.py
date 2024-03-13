from http import HTTPStatus
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/api/echo', methods=['GET'])
def test_hello_world():
    response = hello_world()
    print('test : ',hello_world())
    assert response.status_code == 200
    return response


@app.route('/post', methods=['POST'])
def post():
    params = request.get_json()
    print('???')

    result = jsonify({"data": params, "status": HTTPStatus.OK})

    return result


if __name__ == '__main__':
    app.run(debug=True)