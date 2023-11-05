import os
import json
from processVideo_module import process_video
from helper_functions import download_video_file, get_academic_info, write_results, upload_file

# S3 bucket names
INPUT_BUCKET_NAME = "your-input-bucket-name"
OUTPUT_BUCKET_NAME = "your-output-bucket-name"


import os
import json

def face_recognition_handler(event, context):
	"""
	This function handles the face recognition process. It downloads a video file from an S3 bucket, processes it to recognize a face, retrieves academic information from DynamoDB based on the recognized face, writes the results to a CSV file, and uploads the output file to another S3 bucket.

	Args:
		event (dict): AWS Lambda uses this parameter to pass in event data to the handler.
		context (object): AWS Lambda uses this parameter to provide runtime information to your handler.

	Returns:
		dict: A dictionary containing the status code and a message indicating whether the video was processed successfully or not.
	"""
	# Get the S3 bucket and key from the event
	object_key = event['Records'][0]['s3']['object']['key']
	
	# specify the temp directory to store input, output and intermediate files
	temp_dir = "/tmp"

	# file path to download the video file to
	input_file_path = os.path.join(temp_dir, object_key)

	# download the video file from the S3 bucket to local storage
	is_downloaded = download_video_file(INPUT_BUCKET_NAME, object_key, input_file_path)


	# check if the video file was downloaded successfully
	if not is_downloaded:
		print("Error downloading video file!")
		return {
			'statusCode': 500,
			'body': json.dumps('Error downloading video file!')
		}

	# process the video file and get recognized face name
	result_name = process_video(input_file_path, temp_dir)

	# pull academic information from DynamoDB
	academic_info = get_academic_info(result_name)

	# check if academic information is found
	if academic_info is None:
		print("No academic information found!")
		return {
			'statusCode': 500,
			'body': json.dumps('Error getting academic information!')
		}

	# write the results to a output csv file
	write_results(object_key, academic_info, temp_dir)

	# upload the output file to S3 bucket
	upload_file(OUTPUT_BUCKET_NAME, object_key, temp_dir)

	return {
		'statusCode': 200,
		'body': json.dumps('Successfully processed video!')
	}