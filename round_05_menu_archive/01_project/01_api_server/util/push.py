import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./adminsdk.ignore.json")
firebase_admin.initialize_app(cred)





# Push 메시지 전송 요청 
# users: {list} 메시지를 받을 사용자의 토큰 리스트
# title: {str} 메시지 제목
# body: {str} 메시지 내용
def send_message(users, title, body):

    if(len(users) == 0):
        print("No users")
        return
    
    message = messaging.MulticastMessage(
        data={'title': title,'body': body},
        tokens=users,
    )

    response = messaging.send_multicast(message)

    return response



