# CSV Tool Website

A Streamlit-based web application that provides various tools for working with CSV files. This application includes the following tools:
- CSV Splitter
- CSV to JSON Converter
- File Format Converter
- Row Filtering Tool

## Project Structure
    ├── csv_tool_website
    │   ├── Home.py
    │   ├── pages
    │   │   ├── csv_splitter.py
    │   │   ├── csv_to_json.py
    │   │   ├── file_format_converter.py
    │   │   ├── row_filter.py
    │   ├── uploades
    │   │   ├── (temporary uploaded files and generated zip/json files)
    │   ├── requirements.txt
    │   └── README.md


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/csv_tool_website.git
   cd csv_tool_website
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\Activate.ps1` or `venv\Scripts\activate.bat`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Run the Streamlit application**:
   ```bash
   streamlit run Home.py
   ```

2. **Access the website**:
   Open your web browser and go to `http://localhost:8501`.

## Tools

### CSV Splitter

This tool allows you to split a CSV file into multiple smaller files based on a specified number of rows per file.

1. Upload a CSV file.
2. Enter the number of rows per file.
3. Click the "Split CSV" button to generate the split files.
4. Download the resulting ZIP file containing the split CSV files.

### CSV to JSON Converter

This tool converts a CSV file to JSON format.

1. Upload a CSV file.
2. Click the "Convert to JSON" button.
3. Download the resulting JSON file.

### File Format Converter

This tool converts between different file formats such as Excel (XLSX) to CSV and vice versa.

1. Upload a CSV or Excel file.
2. Select the desired output format (CSV or Excel).
3. Click the "Convert" button.
4. Download the resulting file in the desired format.

### Row Filtering Tool

This tool filters rows in a CSV file based on specific criteria.

1. Upload a CSV file.
2. Select a column to filter by.
3. Depending on the column type (numerical or categorical), specify the filter criteria:
   - For numerical columns: filter by a single value or a range of values.
   - For categorical columns: select a specific value to filter by.
4. Click the "Add Filter" button to add the filter.
5. Repeat the above steps to add more filters if needed.
6. The filtered data will be displayed below the original data.
7. Download the filtered CSV file.

## Contact Us

Use the "Contact Us" section in the application to report bugs, request new features, or send miscellaneous messages. Fill out the form with the necessary details and submit it. You will receive a confirmation message if your submission is successful. The form is made to send a message using a telegram bot by providing the chat ID and the bot http API.
