import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_testing.cdk_testing_stack import CdkTestingStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_testing/cdk_testing_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkTestingStack(app, "cdk-testing")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
