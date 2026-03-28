from pydantic import BaseModel

class UnitCreate(BaseModel):
    vid: int
    lid: int
    sid: int


class UnitResponse(BaseModel):
    uid: int
    vid: int
    lid: int
    sid: int
    status: str 
