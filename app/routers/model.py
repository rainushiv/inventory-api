from fastapi import APIRouter, HTTPException
from ..models.device_model import DeviceModelCreate
import logging
from ..db import database
import logging

router = APIRouter()
logger = logging.getLogger("my_logger")

@router.get("/models", tags=["model"])
async def get_all_models():
    async with database.pool.acquire() as conn: 
        res = await conn.fetch('''SELECT * FROM device_model''') 
        logger.info(f"Called get products and retuned,{res[:2]}...")
    return res 

@router.get("/model/{model_ID}", tags=["model"])
async def get_specific_model(model_ID:int):
    async with database.pool.acquire() as conn: 

        res = await conn.fetch("SELECT * FROM device_model WHERE mid = $1",model_ID) 
        logger.info(f"Called get model with ID: {model_ID} and retuned,{res}")
    return res 



@router.post("/model", tags=["model"])
async def add_model(model:DeviceModelCreate):

    async with database.pool.acquire() as conn: 

        data = await conn.fetch("SELECT * FROM device_model WHERE device_model.pid = $1 or device_model.name = $2",model.pid,model.name.lower()) 
        if data: 

            logger.warning(f"Adding {model.name} in to database as model, but it already exists")
            raise HTTPException(status_code=409,detail="Model already exists within the database")

        res = await conn.fetch("INSERT INTO device_model(pid,name) VALUES ($1,$2) RETURNING * ",model.pid,model.name.lower()) 
    return res 

@router.put("/model/{model_ID}", tags=["model"])
async def edit_model(model_ID:int, new_model_name:DeviceModelCreate):

    async with database.pool.acquire() as conn: 

        data = await conn.fetchrow("SELECT * FROM device_model WHERE device_model.mid = $1",model_ID)
        if not data: 
            logger.error(f"Editing {model_ID} in database, but it doesn't exists")
            raise HTTPException(status_code=404, detail="Model doesnt exists") 


        res = await conn.fetchrow("UPDATE device_model SET name = $1 WHERE mid = $2 RETURNING *",new_model_name.name.lower(),model_ID)

    return res 




@router.delete("/model", tags=["model"])
async def delete_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

