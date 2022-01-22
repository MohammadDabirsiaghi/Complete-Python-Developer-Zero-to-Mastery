# +17069325407
# https://www.twilio.com/
from twilio.rest import Client

account_sid = 'AC115db9630d8059b08590c85742fe83ea'
auth_token = '3c4ff21d0086b86646c5393543973090'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGb34031dbfe0b211f619137c083fab1d1',
    body='سلام پویا',
    to='+989125473894'
)

print(message.sid)
