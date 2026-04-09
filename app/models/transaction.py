from pydantic import BaseModel
from datetime import datetime


class TransactionCreate(BaseModel):
    bid: int #Buyer ID Foregin Key
    price: float
    unit_ids: list[int]  # list of uids being sold in this transaction


class TransactionResponse(BaseModel):
    tid: int
    bid: int
    price: float
    sold_at: datetime