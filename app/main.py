from fastapi import FastAPI
from .routers import product
from .routers import unit 
from .routers import model
from .routers import variant
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from .db import database 
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig( 
        level=logging.INFO,
        format='%(filename)s - %(asctime)s - %(message)s - %(levelname)s', datefmt='%m/%d/%Y %I:%M:%S %p'
      )

logger = logging.getLogger("my_logger")

"""Add File logger rotator """
rotate_file_handler = RotatingFileHandler(filename="logs/log.out",maxBytes= 5 * 1024 * 1024,backupCount=5)
rotate_file_handler.setLevel(logging.ERROR)
format= logging.Formatter('%(filename)s - %(asctime)s - %(message)s - %(levelname)s',datefmt='%m/%d/%Y %I:%M:%S %p')
rotate_file_handler.setFormatter(format)
logger.addHandler(rotate_file_handler)


load_dotenv()

@asynccontextmanager 
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    title="InventoryBackend",
    lifespan=lifespan
)

app.include_router(product.router)
app.include_router(model.router)
app.include_router(variant.router)
app.include_router(unit.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    async with database.pool.acquire() as conn:
        result = await conn.fetchval("SELECT 1")
    return {"db_connected": result == 1}