from pydantic import BaseModel

class LocationCreate(BaseModel):
    name: str 
    address: str


class LocationResponse(BaseModel):
    lid: int
    name: str 
    address: str

