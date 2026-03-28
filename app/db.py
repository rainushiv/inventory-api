from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
import asyncpg
import logging




@asynccontextmanager 
async def lifespan(app: FastAPI):
    app.state.pool = await asyncpg.create_pool(
        host= os.getenv("DB_HOST"), 
        port= int(os.getenv("DB_PORT")),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        database= os.getenv("DB_NAME")
    )
    yield

    await app.state.pool.close()

