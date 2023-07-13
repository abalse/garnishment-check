from getTextFromPdf import pdfReader
from validateFile import fileValidation
import streamlit as st
import json


def main():
    st.set_page_config(page_title="Upload PDF")
    st.header("Garnishment Automation")
    
    pdf = st.file_uploader("Upload your PDF", type = "pdf")
    text = pdfReader(pdf)
    
    if text is None:
        print('Do Nothing')
    elif fileValidation(text) is "Invalid":
        st.error('Context Not related to Garnishment')
    else:
        col1, col2 = st.columns(2)
        response = '{"test":"data"}'
        responseDict = json.loads(response)
        
        # What is the account number of record on whom garnishment notice has been raised?
        # What is the Garnishment Status of garnishment notice raised?
        # What is the Garnishment Type of garnishment notice raised?
        # What is the Garnishment Amount of garnishment notice raised?
        # What are the Garnishment Details of garnishment notice raised?
        # What are the Court Details of raised garnishment notice?
        # {'score': 0.9427658319473267, 'start': 1047, 'end': 1053, 'answer': '7500$.'}
        
        col1.header("People")
        col1.write("This is line 1")
        col1.write("This is line 2")
        
        col2.header("Test")
        col2.write("This is line 3")
        col2.write("This is line 4")
        
        # col3, col4 = st.columns(2)
        
        # col3.header("Money")
        # col3.write("This is line 1")
        # col3.write("This is line 2")
        
        # col4.header("Organization")
        # col4.write("This is line 3")
        # col4.write("This is line 4")

if __name__ == '__main__':
    main()