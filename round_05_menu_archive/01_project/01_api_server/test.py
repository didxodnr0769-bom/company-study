

import requests



# Express 서버 API 요청 테스트
# PROXY_URL = "http://localhost:3000"
PROXY_URL = "https://dont-go-cat-yang.koyeb.app";

# 토큰 목록 조회 API
# GET 요청
response = requests.get(PROXY_URL+"/token/list").json()
# 응답 내용 확인

print(response)
