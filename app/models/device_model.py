from pydantic import BaseModel

class DeviceModelCreate(BaseModel):
    pid: int
    name: str 


class DeviceModelResponse(BaseModel):
    mid: int
    pid: int
    name: str 