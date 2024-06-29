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

st.write("""
Welcome to the CSV Tool Website! Here you can find a variety of tools to help you manage and manipulate your CSV files. Below is a list of available tools and their descriptions:
""")

st.subheader("Tools Available")

st.write("""
**1. CSV Splitter**
- This tool allows you to split a large CSV file into multiple smaller files based on a specified number of rows per file.

**2. CSV to JSON Converter**
- This tool converts a CSV file to JSON format, making it easier to work with in JavaScript applications and other scenarios where JSON is preferred.

**3. File Format Converter**
- This tool converts between different file formats, such as converting an Excel (XLSX) file to CSV and vice versa.

**4. Row Filtering Tool**
- This tool filters rows in a CSV file based on specific criteria, allowing you to easily extract subsets of your data.
""")

st.write("""
Access the tools with the menu on the left.
""")

def display_contact_section(form_key):

    st.header("Contact Us")
    st.write("Use the form below to report bugs, request new tools, or send miscellaneous messages.")

    with st.form(key=form_key):
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

display_contact_section('home')
