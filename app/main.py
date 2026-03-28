from fastapi import FastAPI
from routers import product
from routers import unit 
from routers import item 
from routers import model
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from db import lifespan

load_dotenv()

app = FastAPI(
    title="InventoryBackend",
    lifespan=lifespan
)

app.include_router(product.router)
app.include_router(model.router)
app.include_router(item.router)
app.include_router(unit.router)

@app.get("/")
async def root():
    
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    async with app.state.pool.acquire() as conn:
        result = await conn.fetchval("SELECT 1")
    return {"db_connected": result == 1}