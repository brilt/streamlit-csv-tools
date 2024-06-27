import streamlit as st
import pandas as pd
import os
import uuid

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("CSV Tool Website")

st.sidebar.title("Menu")
tool = st.sidebar.selectbox("Choose a tool", ["Home", "CSV Splitter", "CSV to JSON Converter", "File Format Converter"])

if tool == "Home":
    st.header("Welcome to the CSV Tool Website")
    st.write("Choose a tool from the sidebar to get started.")

elif tool == "CSV Splitter":
    st.header("CSV Splitter")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    rows_per_file = st.number_input("Rows per file", min_value=1, step=1)
    
    if st.button("Split CSV"):
        if uploaded_file is not None and rows_per_file > 0:
            df = pd.read_csv(uploaded_file)
            file_base = os.path.splitext(uploaded_file.name)[0]
            
            temp_dir = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()))
            os.makedirs(temp_dir)
            
            file_parts = []
            for i in range(0, len(df), rows_per_file):
                part_df = df[i:i+rows_per_file]
                part_filename = os.path.join(temp_dir, f'{file_base}_part_{i//rows_per_file + 1}.csv')
                part_df.to_csv(part_filename, index=False)
                file_parts.append(part_filename)
            
            zip_filename = os.path.join(UPLOAD_FOLDER, f'{file_base}_split.zip')
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in file_parts:
                    zipf.write(file, os.path.basename(file))
            
            # Clean up temporary directory
            for file in file_parts:
                os.remove(file)
            os.rmdir(temp_dir)
            
            st.success("CSV file split successfully!")
            with open(zip_filename, 'rb') as f:
                st.download_button('Download ZIP', f, file_name=f'{file_base}_split.zip')
        else:
            st.error("Please upload a CSV file and enter the number of rows per file.")

elif tool == "CSV to JSON Converter":
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

elif tool == "File Format Converter":
    st.header("File Format Converter")
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

    tab1, tab2 = st.tabs(["CSV to Excel (XLSX)", "Excel (XLSX) to CSV"])

    with tab1:
        st.subheader("Convert CSV to Excel (XLSX)")
        if st.button("Convert to Excel (XLSX)"):
            if uploaded_file is not None and uploaded_file.type in ["text/csv", "application/vnd.ms-excel"]:
                file_base = os.path.splitext(uploaded_file.name)[0]
                df = pd.read_csv(uploaded_file)
                excel_filename = os.path.join(UPLOAD_FOLDER, f"{file_base}.xlsx")
                df.to_excel(excel_filename, index=False)

                st.success("CSV file converted to Excel successfully!")
                with open(excel_filename, 'rb') as f:
                    st.download_button('Download Excel', f, file_name=f"{file_base}.xlsx")
            else:
                st.error("Please upload a CSV file.")

    with tab2:
        st.subheader("Convert Excel (XLSX) to CSV")
        if st.button("Convert to CSV"):
            if uploaded_file is not None and uploaded_file.type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
                file_base = os.path.splitext(uploaded_file.name)[0]
                df = pd.read_excel(uploaded_file)
                csv_filename = os.path.join(UPLOAD_FOLDER, f"{file_base}.csv")
                df.to_csv(csv_filename, index=False)

                st.success("Excel file converted to CSV successfully!")
                with open(csv_filename, 'rb') as f:
                    st.download_button('Download CSV', f, file_name=f"{file_base}.csv")
            else:
                st.error("Please upload an Excel file.")