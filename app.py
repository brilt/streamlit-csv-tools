import streamlit as st
from dotenv import load_dotenv
import os
import requests

st.set_page_config(
    page_title="CSV Tool Website",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()  # Take environment variables from .env.


def send_msg(text):
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    token = os.getenv('TELEGRAM_BOT_HTTP_API')
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    return results.json()



st.title("CSV Tool Website")

def display_contact_section():

    st.header("Contact Us")
    st.write("Use the form below to report bugs, request new tools, or send miscellaneous messages.")

    with st.form(key='contact_form'):
        message_type = st.selectbox('Select Message Type', ['Bug Report', 'Feature Request', 'Miscellaneous'])
        user_message = st.text_area("Your Message", placeholder="Describe your issue or suggestion here...")
        submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        if user_message.strip():
            full_message = f"Message Type: {message_type}\n\nMessage:\n{user_message}"
            response = send_msg(full_message)
            if response.get("ok"):
                st.success("Your message has been sent successfully!")
            else:
                st.error("There was an error sending your message. Please try again later.")
        else:
            st.error("Message cannot be empty.")
