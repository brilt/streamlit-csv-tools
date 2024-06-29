import streamlit as st
import pandas as pd
import os
import uuid
import zipfile

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


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
