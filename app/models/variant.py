from pydantic import BaseModel

class VariantCreate(BaseModel):
    mid: int
    SKU: str
    color: str 
    storage: str


class VariantResponse(BaseModel):
    vid: int
    mid: int
    SKU: str
    color: str 
    storage: str



