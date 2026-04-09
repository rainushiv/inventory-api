from fastapi import APIRouter,HTTPException
from ..models.product import ProductCreate,ProductResponse
from ..db import database
import logging
router = APIRouter()
logger = logging.getLogger("my_logger")

@router.get("/products", tags=["product"])
async def get_products():

    async with database.pool.acquire() as conn:
        res = await conn.fetch('''SELECT * FROM product''') 
        logger.info(f"Called get products and retuned,{res[:2]}...")
        
    return res

@router.get("/product/{product_brand}", tags=["product"])
async def get_products(product_brand: str ):

    async with database.pool.acquire() as conn:
        res = await conn.fetch('''SELECT * FROM product WHERE product.brand = $1''',product_brand) 
        logger.info(f"Called get products and retuned,{res}...")
        
    return res



@router.post("/product", tags=["product"])
async def add_product(product: ProductCreate):
    product.brand = product.brand.lower()
    async with database.pool.acquire() as conn:
        data = await conn.fetchrow("SELECT * FROM product WHERE product.brand = $1",product.brand)
        if data:

            logger.error(f"Adding {product.brand} in to database as product, but it already exists")
            raise HTTPException(status_code=409, detail="Product already exists") 

        logger.info(f"Adding {product.brand} in to database as product")
        res = await conn.fetchrow("INSERT INTO product (brand) VALUES ($1) RETURNING *",product.brand)
    
    return res 


@router.put("/product", tags=["product"])
async def edit_product(product:ProductResponse):

    # async with database.pool.acquire() as conn: 

    #     data = await conn.fetchrow("SELECT * FROM product WHERE product.pid = $1",product.pid)
    #     if not data: 
    #         logger.error(f"Editing {product.brand} in database, but it doesn't exists")
    #         raise HTTPException(status_code=404, detail="Product doesnt exists") 


    #     res = await conn.fetchrow("UPDATE Product SET product.brand = $1")

    return [{"Iphone":"Iphone"}] 


@router.delete("/product", tags=["product"])
async def delete_product():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

