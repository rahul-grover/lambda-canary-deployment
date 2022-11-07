import json
import os


def lambda_handler(event, context):
    # if os.environ.get("AWS_LAMBDA_FUNCTION_VERSION"):
    #     raise RuntimeError("This will cause a deployment rollback")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Testing the second lambda function WITH A SUCCESS!!",
        }),
    }
