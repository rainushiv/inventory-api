from pydantic import BaseModel

class SellerCreate(BaseModel):
    name: str 
    phone: str
    email: str


class SellerResponse(BaseModel):
    sid: int
    name: str 
    phone: str
    email: str




