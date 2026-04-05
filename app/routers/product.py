from fastapi import APIRouter
from ..models.product import ProductCreate
from ..db import database
import logging
router = APIRouter()
logger = logging.getLogger("my_logger")

@router.get("/product", tags=["product"])
async def get_products():

    async with database.pool.acquire() as conn:
        res = await conn.fetch('''SELECT * FROM product''') 
        logger.info(f"Called get products and retuned,{res[:2]}...")
        print(res)
        
    return [res]

@router.post("/product", tags=["product"])
async def add_product(product: ProductCreate):
    logger.info(f"Adding {product.brand} in to database as product")
    async with database.pool.acquire() as conn:
        await conn.execute("INSERT INTO product (brand) VALUES ($1)",product.brand)

    
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/product", tags=["product"])
async def edit_product():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/product", tags=["product"])
async def delete_product():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

