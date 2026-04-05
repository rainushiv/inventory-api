from fastapi import APIRouter
from ..models.product import ProductCreate
import logging
router = APIRouter()
logger = logging.getLogger("my_logger")

@router.get("/product", tags=["product"])
async def get_products():

    async with router.state.pool.acquire() as conn:
        res = conn.fetch('''SELECT * FROM product''') 
        logger.info(f"Called get products and retuned,{res}")
        print(res)
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.post("/product", tags=["product"])
async def add_product(product: ProductCreate):

    async with router.state.pool.acquire() as conn:
        conn.execute(f'''INSERT INTO product VALUES ({product.brand})''')

    
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/product", tags=["product"])
async def edit_product():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/product", tags=["product"])
async def delete_product():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

