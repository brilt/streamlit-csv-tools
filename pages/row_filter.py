import streamlit as st
import pandas as pd
import os
from Home import display_contact_section

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def apply_filters(df, filters):
    for f in filters:
        column, filter_type, value = f
        if filter_type == "Single value":
            df = df[df[column] == value]
        elif filter_type == "Range of values":
            min_val, max_val = value
            df = df[(df[column] >= min_val) & (df[column] <= max_val)]
        elif filter_type == "Categorical":
            df = df[df[column] == value]
    return df

st.header("Row Filtering Tool")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if "filters" not in st.session_state:
    st.session_state.filters = []

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    columns = df.columns.tolist()
    
    st.write("### Original Data")
    st.dataframe(df)

    if st.button("Add Filter"):
        st.session_state.filters.append({})
    
    for i, filter_dict in enumerate(st.session_state.filters):
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            column = st.selectbox(f"Column {i+1}", columns, key=f"column_{i}")
        col_type = df[column].dtype

        if pd.api.types.is_numeric_dtype(col_type):
            with col2:
                filter_type = st.radio(f"Type {i+1}", ["Single value", "Range of values"], key=f"type_{i}")
            if filter_type == "Single value":
                with col3:
                    value = st.number_input(f"Value {i+1}", key=f"value_{i}")
                    st.session_state.filters[i] = (column, filter_type, value)
            else:
                with col3:
                    min_value, max_value = st.slider(f"Range {i+1}", float(df[column].min()), float(df[column].max()), (float(df[column].min()), float(df[column].max())), key=f"range_{i}")
                    st.session_state.filters[i] = (column, filter_type, (min_value, max_value))
        else:
            with col2:
                filter_type = "Categorical"
            with col3:
                unique_values = df[column].unique().tolist()
                value = st.selectbox(f"Value {i+1}", unique_values, key=f"value_{i}")
                st.session_state.filters[i] = (column, filter_type, value)

    if st.session_state.filters:
        filtered_df = apply_filters(df, st.session_state.filters)
        
        st.write("### Filtered Data")
        st.dataframe(filtered_df)
        
        filtered_filename = os.path.join(UPLOAD_FOLDER, f"filtered_{uploaded_file.name}")
        filtered_df.to_csv(filtered_filename, index=False)
        
        st.success("Rows filtered successfully!")
        with open(filtered_filename, 'rb') as f:
            st.download_button('Download Filtered CSV', f, file_name=f"filtered_{uploaded_file.name}")

    if st.button("Clear Filters"):
        st.session_state.filters = []
        st.rerun()


display_contact_section('row_filter')