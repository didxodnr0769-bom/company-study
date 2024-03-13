import requests

# GET 요청
response = requests.get('http://127.0.0.1:5000/api')
# 응답 내용 확인
print(response.text)

# POST 요청 (JSON 데이터 전송)
response = requests.post('http://127.0.0.1:5000/post', json={'key': 'value', 'username': 'yangtaewook'})
# JSON 응답 처리
data = response.json()
print(data)