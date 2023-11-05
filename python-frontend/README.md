# README for Python Frontend

This is the frontend interface for the AWS Lambda application, built using Streamlit. The frontend allows users to interact with the project's functionality through a web-based interface.

### Requirements

- Python 3.6 or higher
- AWS account with pre-configured S3 buckets for AWS Lambda
- AWS account with valid AWS credentials
- Streamlit

### File Structure

The main file is `index.py` which imports various components from the `components` directory.

### Components

- `main_section.py`: Contains the function `display_main_section()` which displays the main section of the application.
- `workload_test.py`: Contains the function `workload_test()` which handles the workload testing.
- `upload_file.py`: Contains the function `upload_file()` which handles file uploading.
- `display_results.py`: Contains the functions `display_file_upload_results(object_key)` and `display_workload_results()` which display the results of file upload and workload test respectively.
- `download_results.py`: Contains the function `download_csv(result_data)` which provides a download link for the results.

## Installation and Usage

1. Ensure that you have all the dependencies installed as mentioned in `requirements.txt`

2. To install the dependencies, you can run:
    ```bash
    pip install -r requirements.txt
    ```

3. Update AWS configuration defined in `aws/config.py`:
    - `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID.
    - `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key.
    - `AWS_REGION`: The AWS region where your services are hosted.
    - `AWS_S3_INPUT_BUCKET`: The name of your AWS S3 bucket for input files.
    - `AWS_S3_OUTPUT_BUCKET`: The name of your AWS S3 bucket for output files.

4. To use the frontend, navigate to the directory containing `index.py` and simply run the following command:
    ```bash
    streamlit run index.py
    ```

## Note
- This will start the Streamlit server and the application will be accessible at `localhost:8501` by default.
- You can host the frontend on Streamlit and it's accessible publicly to anyone.