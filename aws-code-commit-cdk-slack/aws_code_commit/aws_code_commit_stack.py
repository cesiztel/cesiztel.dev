from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    aws_chatbot as chatbot
)
from constructs import Construct

class AwsCodeCommitStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a repository
        repo = codecommit.Repository(
            self,
            'Repository',
            repository_name='my-example-repository',
            description='Example of repository'
        )

        target = chatbot.SlackChannelConfiguration(
            self,
            "MySlackChannel",
            slack_channel_configuration_name="pull-requests",
            slack_workspace_id="{MY_WORKSPACE_ID}",
            slack_channel_id="{MY_CHANNEL_ID}"
        )

        repo.notify_on_pull_request_created(
            "NotifyOnPullRequestCreated",
            target
        )