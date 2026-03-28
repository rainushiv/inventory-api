from pydantic import BaseModel

class BuyerCreate(BaseModel):
    name: str 
    phone: str
    email: str


class BuyerResponse(BaseModel):
    bid: int
    name: str 
    phone: str
    email: str



