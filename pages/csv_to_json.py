import streamlit as st
import pandas as pd
import os

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.header("CSV to JSON Converter")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if st.button("Convert to JSON"):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        json_data = df.to_json(orient='records')
        
        json_filename = os.path.join(UPLOAD_FOLDER, f"{os.path.splitext(uploaded_file.name)[0]}.json")
        with open(json_filename, 'w') as json_file:
            json_file.write(json_data)
        
        st.success("CSV file converted to JSON successfully!")
        with open(json_filename, 'rb') as f:
            st.download_button('Download JSON', f, file_name=f"{os.path.splitext(uploaded_file.name)[0]}.json")
    else:
        st.error("Please upload a CSV file.")
