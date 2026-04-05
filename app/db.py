from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
import asyncpg
import logging

logger = logging.getLogger("my_logger")

# @asynccontextmanager 
# async def lifespan(app: FastAPI):
#     app.state.pool = await asyncpg.create_pool(
#         host= os.getenv("DB_HOST"), 
#         port= int(os.getenv("DB_PORT")),
#         user= os.getenv("DB_USER"),
#         password= os.getenv("DB_PASSWORD"),
#         database= os.getenv("DB_NAME")
#     )
#     yield

#     await app.state.pool.close()

class Database:
    def __init__(self):
       logger.info("DB connection started...") 
    async def connect(self):
        try:
            self.pool =  await asyncpg.create_pool(
            host= os.getenv("DB_HOST"), 
            port= int(os.getenv("DB_PORT")),
            user= os.getenv("DB_USER"),
            password= os.getenv("DB_PASSWORD"),
            database= os.getenv("DB_NAME")
        )
        except Exception as exc:
            logger.error(f"DB failed to connect,{exc}")

        logger.info("DB Connected!") 
    async def disconnect(self):
        self.pool.close()

database = Database()

