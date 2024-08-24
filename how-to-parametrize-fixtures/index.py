"""Module to process SQS messages."""
from dataclasses import dataclass
import json
from typing import List

@dataclass
class Order:
    order_number: int
    state: str

def sqs_events_processor(events: dict) -> List[Order]:
    """Process SQS events and translating in list of orders."""
    if "Records" not in events:
        return []
    
    sqs_records = events["Records"]

    orders = []
    for record in sqs_records:
        if "body" not in record:
            continue

        order = json.loads(record["body"])
        orders.append(
            Order(
                order_number=order["order_number"], 
                state=order["event_type"]
            )
        )

    return orders