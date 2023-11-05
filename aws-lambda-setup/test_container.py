# Description: This file is used to test the container locally. It sends a request to the container on port 8080 and prints the response.

import requests
import json

def send_request():
    url = "http://localhost:8080/2015-03-31/functions/function/invocations"
    data = {"Records": [{"s3": {"object": {"key": "test_0.mp4"}}}]}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    return response.json()

print(send_request())