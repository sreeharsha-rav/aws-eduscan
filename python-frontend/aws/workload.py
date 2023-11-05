from boto3 import client as boto3_client
import os
from aws.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

# AWS S3 bucket names
input_bucket = "eduscan-lambda-input"
output_bucket = "eduscan-lambda-output"

# Test cases directory
test_cases = "test_cases/"

# Function to clear input bucket
def clear_input_bucket():
	global input_bucket
	s3 = boto3_client(
		's3',
		region_name = AWS_REGION,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY
		)
	list_obj = s3.list_objects_v2(Bucket=input_bucket)
	try:
		for item in list_obj["Contents"]:
			key = item["Key"]
			s3.delete_object(Bucket=input_bucket, Key=key)
		print("Input bucket cleared")
	except:
		print("Nothing to clear in input bucket")

# Function to clear output bucket
def clear_output_bucket():
	global output_bucket
	s3 = boto3_client(
		's3',
		region_name = AWS_REGION,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY
		)
	list_obj = s3.list_objects_v2(Bucket=output_bucket)
	try:
		for item in list_obj["Contents"]:
			key = item["Key"]
			s3.delete_object(Bucket=output_bucket, Key=key)
		print("Output bucket cleared")
	except:
		print("Nothing to clear in output bucket")

# Function to upload to input bucket
def upload_to_input_bucket_s3(path, name):
	global input_bucket
	s3 = boto3_client(
		's3',
		region_name = AWS_REGION,
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY
		)
	s3.upload_file(path + name, input_bucket, name)
	
# Function to upload to output bucket
def upload_files(test_case):	
	global input_bucket
	global output_bucket
	global test_cases
	
	
	# Directory of test case
	test_dir = test_cases + test_case + "/"
	
	# Iterate over each video
	# Upload to S3 input bucket
	for filename in os.listdir(test_dir):
		if filename.endswith(".mp4") or filename.endswith(".MP4"):
			print("Uploading to input bucket..  name: " + str(filename)) 
			upload_to_input_bucket_s3(test_dir, filename)
			
# Function to run workload generator
def workload_generator(test_case = "test_case_1"):
	
	print(f"Running workload generator for {test_case}..")
	upload_files(test_case)
	
# Function to run workload
def run_workload(test_case):
	clear_input_bucket()
	clear_output_bucket()	
	workload_generator(test_case)