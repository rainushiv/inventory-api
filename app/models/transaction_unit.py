from pydantic import BaseModel


class TransactionUnitCreate(BaseModel):
    tid: int
    uid: int


class TransactionUnitResponse(BaseModel):
    tid: int
    uid: int