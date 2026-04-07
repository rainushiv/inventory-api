from fastapi import APIRouter
from ..models.device_model import DeviceModelCreate
import logging
from ..db import database
import logging

router = APIRouter()
logger = logging.getLogger("my_logger")
@router.get("/model", tags=["model"])
async def get_models():
    async with database.pool.acquire() as conn: 
        res = await conn.fetch('''SELECT * FROM device_model''') 
        logger.info(f"Called get products and retuned,{res[:2]}...")
    return res 

@router.post("/model", tags=["model"])
async def add_model(model:DeviceModelCreate):

    async with database.pool.acquire() as conn: 
        res = await conn.fetch("INSERT INTO device_model(pid,name) VALUES ($1,$2)",model.pid,model.name) 
    return res 

@router.put("/model", tags=["model"])
async def edit_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/model", tags=["model"])
async def delete_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

