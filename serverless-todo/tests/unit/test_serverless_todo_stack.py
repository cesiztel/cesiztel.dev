import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_todo.serverless_todo_stack import ServerlessTodoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_todo/serverless_todo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessTodoStack(app, "serverless-todo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
