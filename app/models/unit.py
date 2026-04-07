from pydantic import BaseModel

class UnitCreate(BaseModel):
    vid: int #Variant ID Foreign Key
    lid: int #Location ID Foreign Key
    sid: int #Seller ID Foreign Key


class UnitResponse(BaseModel):
    uid: int
    vid: int
    lid: int
    sid: int
    status: str 
