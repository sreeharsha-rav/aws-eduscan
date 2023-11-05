"""
Module to interact with AWS S3
"""
import os
import boto3

from aws.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION


class AWS_S3Client:
    """
    AWS S3 interaction class
    """
    def __init__(self):
        """
        Intialize an S3 client
        """
        self.s3_client = boto3.client(
            's3',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

    def upload_video(self, bucket_name, local_file_path):
        """
        Function to upload a video to an S3 bucket
        """
        try:
            file_name = os.path.splitext(os.path.basename(local_file_path))[0] + '.mp4'
            s3_object_key = file_name  # Use the base name as the S3 object key

            self.s3_client.upload_file(local_file_path, bucket_name, s3_object_key)
            print(f"Uploaded {local_file_path} to s3://{bucket_name}/{s3_object_key}")

            return s3_object_key

        except:
            print(f"Error uploading {local_file_path} to S3.")
            return None

    def download_single_result(self, bucket_name, object_key):
        """
        Function to download single result from an S3 bucket using the object key
        """
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=object_key)
            data = response['Body'].read().decode('utf-8')
            # Split the data into rows, assuming it's in CSV format
            rows = data.strip().split('\n')
            # Process the data into a list of dictionaries
            data_list = []
            for row in rows:
                file, name, major, year = row.split(',')
                data_list.append({'File': file, 'Name': name, 'Major': major, 'Year': year})
            print(f"Successfully downloaded {object_key} from S3.")
            return data_list
        except:
            print("Error downloading data from S3.")
            return None

    def get_num_of_results(self, bucket_name):
        """
        Function to get the number of results in an S3 bucket
        """
        try:
            # Get a list of objects in the bucket
            s3_objects = self.s3_client.list_objects(Bucket=bucket_name)

            # Return the number of objects in the bucket
            return len(s3_objects.get('Contents', []))

        except:
            print("Error downloading data from S3.")
            return None

    def download_all_results(self, bucket_name):
        """
        Function to download all results from an S3 bucket
        """
        try:
            # Get a list of objects in the bucket
            s3_objects = self.s3_client.list_objects(Bucket=bucket_name)

            # Download CSV files and store their contents in a list
            csv_data = []
            for s3_object in s3_objects.get('Contents', []):
                s3_object_key = s3_object['Key']
                response = self.s3_client.get_object(Bucket=bucket_name, Key=s3_object_key)
                csv_content = response['Body'].read().decode('utf-8')
                csv_data.append(csv_content)

            # Return the list of CSV data
            return csv_data

        except:
            print("Error downloading data from S3.")
            return None