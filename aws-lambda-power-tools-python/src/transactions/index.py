from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Tracer

from transactions_controller import TransactionsController

tracer = Tracer()
app = APIGatewayRestResolver()
transactions_controller = TransactionsController()


@app.get("/transactions")
@tracer.capture_method
def list_transactions():
    return transactions_controller.list()


@app.post("/transactions")
def create_transaction():
    transaction_data: dict = app.current_event.json_body  # deserialize json str to dict
    return transactions_controller.create(
        transaction_data["amount"],
        transaction_data["type"],
        transaction_data["category"],
    )


@app.get("/transactions/<transaction_id>")
@tracer.capture_method
def get_transaction(transaction_id: str):
    tracer.put_metadata(key="Transaction Id", value=f"{transaction_id}")

    return transactions_controller.find(transaction_id)


@app.delete("/transactions/<transaction_id>")
@tracer.capture_method
def delete_transaction(transaction_id: str):
    tracer.put_metadata(key="Transaction Id", value=f"{transaction_id}")

    return transactions_controller.delete(transaction_id)


@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext):
    return app.resolve(event, context)
