import os,re
from twilio.rest import Client



def validNumber(phone_nuber):
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACe295f7fbece406981546347f2b5986c2']
auth_token = os.environ['0454d526060caeb3e6c9191026a78bb3']
client = Client(account_sid, auth_token)

message_body = input("Enter what do you want to send:")
message_destination = input("Enter where do you want to send the message:")

while not validNumber(message_destination):
    print("INVALID PHONE NUMBER!!!")
    message_destination = input("Enter where do you want to send the message:")


message = client.messages 
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12184034263',
                     to=message_destination
                 )
print(message.sid)
