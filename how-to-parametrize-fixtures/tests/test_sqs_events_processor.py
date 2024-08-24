import pytest
from index import sqs_events_processor

@pytest.fixture(name="sqs_envelope")
def fixture_sqs_envelope():
    yield { "Records": [] }


@pytest.fixture(name="one_confirmed_order")
def fixture_one_confirmed_order(sqs_envelope):
    sqs_envelope["Records"].append(
        {
            "messageId": "f2756a8a-ea58-4b9c-8f04-5c9253564144",
            "body": '{"event_type": "OrderConfirmed", "order_number": 11111}',
            "messageAttributes": {}
        }
    )

    yield sqs_envelope

@pytest.fixture(name="two_orders")
def fixture_two_orders(one_confirmed_order):
    one_confirmed_order["Records"].append(
        {
            "messageId": "f2756a8a-ea58-4b9c-8f04-5c9253564144",
            "body": '{"event_type": "OrderCanceled", "order_number": 22222}',
            "messageAttributes": {}
        }
    )

    yield one_confirmed_order


@pytest.mark.parametrize(
  "sqs_records_fixture", 
  [
    "sqs_envelope",
    "one_confirmed_order",
    "two_orders"
  ]
)
def test_processing_queue_messages(sqs_records_fixture, request):
    """Testing the processing of SQS messages."""
    
    # ARRANGE
    sqs_records = request.getfixturevalue(sqs_records_fixture)

    # ACT
    orders = sqs_events_processor(sqs_records)

    # ASSERT
    # We can create the objects Order and pass them as parameters too.
    # Doing this for simplicity of the example.
    if sqs_records_fixture == "sqs_envelope":
        assert len(orders) == 0

    if sqs_records_fixture == "one_confirmed_order":
        assert len(orders) == 1
        assert orders[0].order_number == 11111
        assert orders[0].state == "OrderConfirmed"

    if sqs_records_fixture == "two_orders":
        assert len(orders) == 2
        assert orders[0].order_number == 11111
        assert orders[0].state == "OrderConfirmed"
        assert orders[1].order_number == 22222
        assert orders[1].state == "OrderCanceled"
