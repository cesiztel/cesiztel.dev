from aws_cdk import Stack, aws_lambda as _lambda
from constructs import Construct


class AwsLambdaPowerToolsPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Add powertools as lambda layer
        powertools_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            id="lambda-powertools",
            layer_version_arn=f"arn:aws:lambda:{self.region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:32",
        )

        # Create lambda and add Power tools
        transaction_handler_function = _lambda.Function(
            self,
            "TransactionsFunctionHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda/transactions"),
            handler="index.handler",
            layers=[powertools_layer],
        )
