from pydantic import BaseModel

class DeviceModelCreate(BaseModel):
    pid: int # Product ID foreign Key
    name: str 


class DeviceModelResponse(BaseModel):
    mid: int
    pid: int
    name: str 