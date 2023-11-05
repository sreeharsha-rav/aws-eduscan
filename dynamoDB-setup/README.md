# README for AWS DynamoDB Setup

## Description
The `dynamoDB_init.py` script is used to create a DynamoDB table named 'Students' and populate it with data. The data is loaded from a JSON file named `student_data.json`.

## Requirements
- Python 3.x
- `boto3` Python library
- AWS account with DynamoDB access
- AWS credentials (Access Key ID and Secret Access Key)

## Usage
1. In `dyanmoDB_init.py`, replace `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` with your actual AWS credentials.
2. Ensure that the `student_data.json` file is in the same directory as the script. The JSON file should contain an array of student objects, each with 'name', 'major', and 'year' attributes.
3. Run the script using Python 3.x.

## Output
The script will create a DynamoDB table named 'Students' with 'name' as the partition key. It will then populate the table with student data from the `student_data.json` file. The script will print a success message if the table creation and data insertion are successful. If there are any errors, they will be printed to the console.

## Note
Ensure that the AWS region in the script matches the region of your AWS account. The default region in the script is 'us-east-1'.