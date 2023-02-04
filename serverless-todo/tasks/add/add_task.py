import json

def handler(event, context):
    # Returns success reponse to API Gateway
    return {
        "statusCode": 200,
        "body": json.dumps(event),
    }