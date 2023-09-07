"""Module that manage all the operations for transactions."""

from enum import Enum
import uuid
from datetime import datetime


class ItemNotFoundException(Exception):
    """Raised when the transaction is not found."""


class TransactionsType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionsController:
    """Controller for transactions operations."""

    def __init__(self) -> None:
        self._fake_transaction = {
            "id": str(uuid.uuid4()),
            "amount": 100,
            "type": TransactionsType.INCOME.value,
            "category": "grocery",
            "created_at": str(datetime.now()),
        }

    def list(self):
        """List all transactions."""
        return [
            self._fake_transaction,
        ]

    def create(self, amount: float, type: str, category: str):
        """Create a new transaction."""
        return {
            "id": str(uuid.uuid4()),
            "amount": amount,
            "type": TransactionsType(type).value,
            "category": category,
            "created_at": str(datetime.now()),
        }

    def find(self, id: str):
        """Find a single transaction."""
        if id == self._fake_transaction["id"]:
            return self._fake_transaction
        else:
            raise ItemNotFoundException(f"Transaction with id {id} not found")

    def delete(self, id: str):
        """Delete a single transaction."""
        self._fake_transaction["id"] = id
        return self._fake_transaction
