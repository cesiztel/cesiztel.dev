import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_code_commit.aws_code_commit_stack import AwsCodeCommitStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_code_commit/aws_code_commit_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCodeCommitStack(app, "aws-code-commit")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
