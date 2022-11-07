import json
import os

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Testing the first lambda function!!"
        }),
    }
