from flask import Flask, request
from pymessenger.bot import Bot
import random

app = Flask(__name__)
ACCESS_TOKEN = 'EAAGdIZANGm3kBO3NXyBi8DmJxcPdfgVLnOAAEZADloYP5K2u1P4aVpwoKYUK3vKiadzs5irF7amfpM3nWG1UoTztgkyOUZC941hEKDNlTc5Pw675dftgg6RleZBJ8xKY0PQLnd4XeLqCrzZB9Q0Ozn6XffllpJfZBvuVDkCIr8bKNIIwAhjPzHjtrWdabaJMf3vAZDZD'
VERIFY_TOKEN = '8a8d0a9e0cd0fe6b5ab0b97805c2e537'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
    
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
        return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

def get_message():
    sample_responses = ["Hello!", "Hi there!", "How can I help you?"]
    return random.choice(sample_responses)

if __name__ == "__main__":
    app.run()
