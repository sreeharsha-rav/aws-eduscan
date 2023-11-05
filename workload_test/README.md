# README for Workload Test

This Python script is used to manage and run workloads on AWS S3 buckets. It provides functionalities to clear input and output buckets, upload files to these buckets, and run workload generators.

## Functions

- `clear_input_bucket()`: This function clears all the contents of the input bucket.
- `clear_output_bucket()`: This function clears all the contents of the output bucket.
- `upload_to_input_bucket_s3(path, name)`: This function uploads a file to the input bucket. The file to be uploaded is specified by its path and name.
- `upload_files(test_case)`: This function uploads all .mp4 files in a specified test case directory to the input bucket.
- `workload_generator()`: This function runs the workload generator. It uploads files for two test cases.

## Usage
To run the script, use the following command:

```bash
python workload.py
```

## Requirements
- AWS S3 buckets for input and output, provide bucket names in `workload.py`.
- AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION) must be set in the `config.py` file.
- Test case directories containing .mp4 files for testing.

## Note
This script uses the boto3 AWS SDK for Python to interact with AWS S3. Make sure to install it using pip:

```bash
pip install boto3
```