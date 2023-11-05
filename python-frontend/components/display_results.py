import streamlit as st
import pandas as pd
import os
import time
from aws.s3_module import AWS_S3Client
from aws.config import AWS_S3_OUTPUT_BUCKET

# Function to display the results of a file upload
def display_file_upload_results(object_key):
    # convert object key to csv file name
    csv_object_key = os.path.splitext(object_key)[0] + '.csv'
    s3_client = AWS_S3Client()

    # Wait for the results to be available
    while True:
        data = s3_client.download_single_result(AWS_S3_OUTPUT_BUCKET, csv_object_key)
        if data:
            break
        time.sleep(5)

    # Create a dataframe from the results
    df = pd.DataFrame(data)
    st.dataframe(df)

    return data

# Function to display the results of workload generator
def display_workload_results():
    s3_client = AWS_S3Client()

    data = s3_client.download_all_results(AWS_S3_OUTPUT_BUCKET)
    
    if data:
        # Split each string into individual data elements
        data_entries = [entry.strip().split(',') for entry in data]
        # Create a list of dictionaries with keys 'File', 'Name', 'Major', and 'Year'
        data_dicts = [
            {
                'File': entry[0],
                'Name': entry[1],
                'Major': entry[2],
                'Year': entry[3]
            }
            for entry in data_entries
        ]
        # Create a dataframe from the list of dictionaries
        df = pd.DataFrame(data_dicts)
        st.dataframe(df)
        return data_dicts
    else:
        st.info('🚫 No results to display ')
        return []