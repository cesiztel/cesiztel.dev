from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext

from transactions_controller import TransactionsController

app = APIGatewayRestResolver()
transactions_controller = TransactionsController()


@app.get("/transactions")
def list():
    return transactions_controller.list()


@app.post("/transactions")
def create():
    transaction_data: dict = app.current_event.json_body  # deserialize json str to dict
    return transactions_controller.create(
        transaction_data["amount"],
        transaction_data["type"],
        transaction_data["category"],
    )


@app.get("/transactions/<transaction_id>")
def find(transaction_id: str):
    return transactions_controller.find(transaction_id)


@app.delete("/transactions/<transaction_id>")
def delete_transaction(transaction_id: str):
    return transactions_controller.delete(transaction_id)


def handler(event: dict, context: LambdaContext):
    return app.resolve(event, context)
