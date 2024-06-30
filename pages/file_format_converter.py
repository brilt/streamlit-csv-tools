import streamlit as st
import pandas as pd
import os
from app import display_contact_section

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.header("File Format Converter")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"])
conversion_type = st.selectbox("Convert to", ["CSV", "Excel (XLSX)"])

if st.button("Convert"):
    if uploaded_file is not None:
        file_base = os.path.splitext(uploaded_file.name)[0]
        if conversion_type == "CSV" and uploaded_file.type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
            df = pd.read_excel(uploaded_file)
            csv_filename = os.path.join(UPLOAD_FOLDER, f"{file_base}.csv")
            df.to_csv(csv_filename, index=False)
            
            st.success("Excel file converted to CSV successfully!")
            with open(csv_filename, 'rb') as f:
                st.download_button('Download CSV', f, file_name=f"{file_base}.csv")
        elif conversion_type == "Excel (XLSX)" and uploaded_file.type in ["text/csv", "application/vnd.ms-excel"]:
            df = pd.read_csv(uploaded_file)
            excel_filename = os.path.join(UPLOAD_FOLDER, f"{file_base}.xlsx")
            df.to_excel(excel_filename, index=False)
            
            st.success("CSV file converted to Excel successfully!")
            with open(excel_filename, 'rb') as f:
                st.download_button('Download Excel', f, file_name=f"{file_base}.xlsx")
        else:
            st.error("Invalid file format for the selected conversion.")
    else:
        st.error("Please upload a file.")

display_contact_section('file_format_converter')