import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_lambda_power_tools_python.aws_lambda_power_tools_python_stack import AwsLambdaPowerToolsPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_lambda_power_tools_python/aws_lambda_power_tools_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsLambdaPowerToolsPythonStack(app, "aws-lambda-power-tools-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
