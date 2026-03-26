from fastapi import FastAPI
from routers import product
from routers import unit 
from routers import item 
from routers import model
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import asyncpg

load_dotenv()

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

    await app.state.poop.close()


app = FastAPI(
    title="InventoryBackend"
)

app.include_router(product.router)
app.include_router(model.router)
app.include_router(item.router)
app.include_router(unit.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}