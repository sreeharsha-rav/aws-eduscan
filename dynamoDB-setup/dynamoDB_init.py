# Description: This file creates a DynamoDB table and populates it with data

import boto3
import json

# AWS Credentials
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'

# Create a DynamoDB Table and populate it with data
dynamodb = boto3.client(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

try:
    # CREATE TABLE
    table = dynamodb.create_table(
        TableName='Students',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table created successfully!")

except Exception as e:
    print("Error creating table:")
    print(e)

try:
    # INSERT DATA
    # Load student data from the JSON file
    with open('student_data.json', 'r') as f:
        students = json.load(f)

    # Insert each student into the DynamoDB table
    for student in students:
        dynamodb.put_item(
            TableName='Students',
            Item={

                'name': {'S': student['name']},
                'major': {'S': student['major']},
                'year': {'S': student['year']}
            }
        )

    print("Data inserted successfully!")

except Exception as e:
    print("Error inserting data into table:")
    print(e)