from aws_cdk import Stack, aws_lambda as _lambda, aws_apigateway as apigw
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
            code=_lambda.Code.from_asset("functions/transactions"),
            handler="index.handler",
            layers=[powertools_layer],
        )

        # Create API Gateway - Lambda integration
        api = apigw.LambdaRestApi(
            self,
            "FinanceAppApiLambdaIntegration",
            handler=transaction_handler_function,
        )

        # Set up endpoints
        transactions = api.root.add_resource("transactions")
        transactions.add_method("GET")  # GET /transactions
        transactions.add_method("POST")  # POST /transactions

        transaction = transactions.add_resource("{transaction_id}")
        transaction.add_method("GET")  # GET /transactions/{transaction_id}
        transaction.add_method("DELETE")  # DELETE /transactions/{transaction_id}
