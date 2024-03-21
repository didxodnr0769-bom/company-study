import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./test-adminsdk.ignore.json")
firebase_admin.initialize_app(cred)




registration_token = 'coy_761o2Cx-qOt4M1VZPd:APA91bGRAwvfSdvHiEIhcREwyyOdJbqSXAyojkppxxQKxBiyDnUFAH3AuuXg_YXQsD6NmqI_yE26qcn9_gSbOMNTRI99G9EZ52d9lXTXhGhXcp4ldKkShBNGjLoEiq15gMDbr5DWMgf-'
message = messaging.Message(
    # notification = messaging.Notification(
    #     title='공지가 업데이트 되었습니다. 확인해주세요',
    #     body='python!.'
    # ),
    data={
        'title': '공지가 업데이트 되었습니다. 확인해주세요',
        'body': 'python!.'
    },
    token=registration_token,
    # android=messaging.AndroidConfig(
    #     # ttl=datetime.timedelta(seconds=3600),
    #     priority='normal',
    #     notification=messaging.AndroidNotification(
    #         icon='stock_ticker_update',
    #         color='#f45342'
    #     ),
    # ),
    # apns=messaging.APNSConfig(
    #     payload=messaging.APNSPayload(
    #         aps=messaging.Aps(badge=42),
    #     ),
    # ),
    # topic='industry-tech',
)

response = messaging.send(message)
print('Successfully sent message:', response)