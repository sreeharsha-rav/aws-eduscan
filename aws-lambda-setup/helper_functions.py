import boto3
import os

# AWS Credentials
AWS_ACCESS_KEY_ID = "your-access-key-id"
AWS_SECRET_ACCESS_KEY = "your-secret-access-key"

# DynamoDB table name
TABLE_NAME = "Students"
PARTITION_KEY = "name"

# Function to pull a video file from S3 bucket
def download_video_file(bucket_name, object_key, file_path):
    # create an S3 client
    s3_client = boto3.client(
        's3',
        region_name = "us-east-1",
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )
    # download the video file from the S3 bucket to local storage
    try:
        s3_client.download_file(bucket_name, object_key, file_path)
        print("File downloaded successfully!")
        return True
    except Exception as e:
        print(f"Error downloading video from S3: {str(e)}")
        return False

# Function to pull academic information from DynamoDB
def get_academic_info(name):
    # create a DynamoDB client
    dynamodb_client = boto3.client(
        'dynamodb',
        region_name = "us-east-1",
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )
    # get the academic information from DynamoDB
    try:
        response = dynamodb_client.get_item(
            TableName = TABLE_NAME,
            Key = {
                PARTITION_KEY: {
                    'S': name
                }
            }
        )
        print("Data retrieved successfully!")
        return response['Item']
    except Exception as e:
        print(f"Error retrieving data from DynamoDB: {str(e)}")
        return None

# Function to write results to a output file
def write_results(input_file, academic_info, output_dir):
    # extract the input file name
    input_name = os.path.splitext(input_file)[0]
    # create the output file path
    output_file_path = os.path.join(output_dir,  input_name + ".csv")
    # write the results to the output file
    with open(output_file_path, 'w') as csvfile:
        csvfile.write(f"{input_file},{academic_info['name']['S']},{academic_info['major']['S']},{academic_info['year']['S']}\n")

# Function to upload a file to S3 bucket
def upload_file(bucket_name, object_name, output_dir):
    # create object key
    object_key = os.path.splitext(object_name)[0] + ".csv"
    # get output file path
    file_path = os.path.join(output_dir, object_key)
    # create an S3 client
    s3_client = boto3.client(
        's3',
        region_name = "us-east-1",
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )
    # upload the file to S3 bucket
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print("File uploaded successfully!")
    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")