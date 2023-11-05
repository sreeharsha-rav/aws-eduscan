# EduScan

*A classroom assistant for seamless student identification and academic data retrieval.*

## Project Description
Eduscan is a python application that uses AWS Lambda and related services to process uploaded classroom videos, recognize students' faces and retrieve academic data.

**Key Tasks:**

1. **Video Upload**: Users upload videos to an S3 input bucket.

2. **Video Processing**: Lambda function processes videos, extracts frames, and recognizes faces.

3. **Face Recognition**: Academic data is retrieved based on recognized faces from DynamoDB.

4. **Data Preloading**: Student data is preloaded into DynamoDB.

5. **Custom Lambda Function**: Utilize a custom container image with preinstalled tools for Lambda.

6. **Academic Data Storage**: Store academic info in CSV format in an S3 output bucket.

7. **Testing**: Sample videos and workload generator for testing.

**Deliverables:**

- User-friendly UI for video uploads.
- AWS Lambda for video processing.
- DynamoDB preloading with academic data.
- Properly formatted content in the output S3 bucket.
- Sample videos for testing.
- Workload generator for validation.

This project aims to enhance classroom management with efficient student recognition and data retrieval.

## Installation and Usage

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- AWS account with access to S3, ECR, Lambda, DynamoDB
- Streamlit
- VS Code

### Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/sreeharsha-rav/aws-eduscan.git
   ```

2. Navigate to the project folder:
   ```sh
   cd aws-eduscan
   ```

3. Go to the `dynamoDB-setup` folder and use the code to set up DynamoDB.

4. Go to the `aws-lambda-setup` folder and use the code to set up AWS Lambda.

5. Create a virtual environment (optional):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

6. Go to the `python-frontend` folder and follow the instructions to run the frontend.

## Note
- To run tests for AWS Lambda locally on terminal goto `workload_test` folder and follow instructions.

## Credits

This project is part of CSE 546 - Cloud Computing course curriculum at ASU.