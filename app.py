import os
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from mkv import ask, append_interaction_to_chat_log


app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route('/', methods=['POST'])
def jabe():
    incoming_msg = request.form.get('message')
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return {"response":answer}

if __name__ == '__main__':
    app.run() 