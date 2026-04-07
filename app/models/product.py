from pydantic import BaseModel

class ProductCreate(BaseModel):
    brand: str 


class ProductResponse(BaseModel):
    pid: int # Product ID
    brand: str 
    