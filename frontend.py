import requests
import os
import streamlit as st
from mkv import ask,append_interaction_to_chat_log
from twilio.twiml.messaging_response import MessagingResponse
from mkv import ask, append_interaction_to_chat_log

st.title("Talent AI")

session = {}
input = st.text_area("Type in a message",key='text')

def ask_question(incoming_msg):
    '''Ask a question'''
    try:
        chat_log = session.get('chat_log')
        answer = ask(incoming_msg, chat_log)
        session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                            chat_log)
        return True, answer
    except Exception as e:
        print(e)
        return False, "There was an error"

    
def on_submit():
    '''On submit button'''
    content = input.lstrip().rstrip()
    if len(content) > 0:
        success, message = ask_question(content)
        if success:
            st.session_state["text"] = ""
            st.write(message) 
        else:
            st.error(message)
    else:
        st.error("Please enter in text")

st.button("Submit",on_click=on_submit)
