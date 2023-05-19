import aws_lambda_powertools


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": f"AWS Lambda powertools author: {aws_lambda_powertools.__author__}",
    }
