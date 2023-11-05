# README for AWS Lambda Setup

## Description
The script `handler.py` contains the function `face_recognition_handler`, which handles the face recognition process. It downloads a video file from an S3 bucket, processes it to recognize a face, retrieves academic information from DynamoDB based on the recognized face, writes the results to a CSV file, and uploads the output file to another S3 bucket.

## Requirements
- Python 3.x
- An AWS account with two S3 buckets already set up, including bucket names.
- An AWS account with a DynamoDB table already set up, including the table name and partition key.
- An AWS account with Elastic Container Registry (ECR) access.
- AWS credentials (Access Key ID and Secret Access Key).
- Docker.
- AWS Command Line Interface (CLI).

## Usage
1. In `handler.py`, replace `INPUT_BUCKET_NAME` and `OUTPUT_BUCKET_NAME` with your actual AWS S3 bucket names.
2. In `helper_functions.py`, replace `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` with your actual AWS credentials, and replace `TABLE_NAME` and `PARTITION_KEY` with your actual DynamoDB details.
3. (Optional) Build a Docker image and test it locally:
    1. Build the Docker Image
    ```bash
    docker build -t your-image-name .
    ```
    2. Run the Docker image
    ```bash
    docker run -p 8080:8080 your-image-name
    ```
    3. Test the Docker container with `test_container.py` to ensure that it works locally.
4. Create a repository in AWS ECR, view push commands, and follow them to push the Docker image to AWS.
5. Create an AWS Lambda function from the AWS Management Console, build it from the existing container in AWS ECR.
6. Add a trigger to AWS Lambda for S3 object creation events.
7. Change the general configuration of AWS Lambda: edit memory to increase it to 1024 MB, edit ephemeral storage to increase it to 4096 MB, and edit the timeout to increase it to 2 minutes.
8. Test the AWS Lambda function with an S3 PUT event template. Make sure to use an appropriate object key.

## Output
- Building the Docker image and running it locally allows you to test the Lambda function in an environment similar to AWS Lambda.
- You will have a Docker image repository set up in AWS Elastic Container Registry (ECR), and the image will be ready for deployment.
- Your Lambda function will be created using the Docker image stored in ECR as its runtime.
- Your Lambda function will be set up to automatically trigger when new objects are created in the specified S3 bucket.
- Your Lambda function will have updated memory allocation, storage, and timeout settings to accommodate its processing requirements.
- You can use an S3 PUT event template to test your Lambda function. Ensure that the function processes objects with the specified object key correctly.

## Notes
- Configuring the `entry.sh` file correctly is essential to ensure compatibility with your operating system. This code builds a container on Windows, so the configuration of `entry.sh` is Dos2Unix (LF). If you are on Mac/Linux, you need to change the configuration of `entry.sh` to Unix (CRLF). This can be easily done in VSCode.
- Choose the appropriate architecture (x86 or arm64) when creating the Lambda function to match the platform where the container image was created.
- Confirm that the AWS region specified in the script matches your AWS account's region to ensure seamless execution. The default region in the script is 'us-east-1'.