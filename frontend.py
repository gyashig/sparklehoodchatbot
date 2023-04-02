import requests
import streamlit as st
st.title("Talent AI")

BACKEND_URL = "http://127.0.0.1:8000"

input = st.text_area("Type in a message",key='text')

def clear_text():
    st.session_state["text"] = ""

def get_response(text):
    res = requests.post(BACKEND_URL,json={"message":text})
    if res.ok:
        message = res.json().get("response")
        return True, message
    else:
        print(res.content)
        return False, "There was an error"
    
def on_submit():
    content = input.lstrip().rstrip()
    if len(content) > 0:
        success, message = get_response(content)
        if success:
            clear_text()
            st.write(message) 
        else:
            st.error(message)
    else:
        st.error("Please enter in text")

st.button("Submit",on_click=on_submit)

