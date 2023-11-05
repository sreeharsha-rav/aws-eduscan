import streamlit as st
import tempfile
import os
from aws.s3_module import AWS_S3Client

def upload_file():
    st.sidebar.title("Upload 📤")
    st.sidebar.subheader('Input mp4 file')
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["mp4"])

    if uploaded_file is not None:
        # Create a temporary directory to store the uploaded file
        temp_dir = tempfile.TemporaryDirectory()
        temp_file_path = os.path.join(temp_dir.name, uploaded_file.name)

        # Save the uploaded file to the temporary location
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Upload file to AWS S3
        s3_client = AWS_S3Client()
        object_key = s3_client.upload_video('eduscan-lambda-input', temp_file_path)
        st.sidebar.info(f'✅ File successfully uploaded. Object key: {object_key}')

        # Cleanup the temporary directory
        temp_dir.cleanup()
        
        return True, object_key
    else:
        st.sidebar.info('☝️ Upload an mp4 file')
        return False, None