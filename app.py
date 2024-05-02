from flask import Flask, request
from pymessenger.bot import Bot
import random

app = Flask(__name__)
ACCESS_TOKEN = 'EAAQxS0IAz3oBO6rqdXiYlC3XUUjmwpdtjQZCsXDaWRra321HzgNfcGK5YDiem7zDGy0VM5lTkmZBVl3GQdWUrRbXExxxwyTUbIf6UEQ61ZBMZBs3KNpgOk4M7Vki28cRAESRNcQOPUzivGcTqAc75OBGHFkxh1tn3PJxzejOYDipzhH72o15Hyk68GiFb6tXFdZBQjV4TwPZAx0enqu5ZBubbBl4z2lzkRZACNLcOydnK9QhGWxUhrNJxWmiDg4cOVBiS8KyhmEZBTzwZD'
VERIFY_TOKEN = 'afc7b8b931b6a2bfb07e0e58659dc1aa'
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
