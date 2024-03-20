import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./test-adminsdk.json")
firebase_admin.initialize_app(cred)




registration_token = 'dUrjZljnbuLSqhZrxNR401:APA91bFXjVdbYyeJg6l9iSTVFFXcWrT3agKKXh_o7DW_sb2J9-QX_FccrVekMfWJYWAbuv8xbi7_t-EoUsqdqBMx92WO6fiFCyrDjXptMeJ24sY0liu3dxOHFMiVKdP__KKTs8T8WXjf'
message = messaging.Message(
    notification = messaging.Notification(
        title='ㅅㄷㄴㅅ!',
        body='body'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)