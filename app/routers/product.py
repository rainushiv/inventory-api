from fastapi import APIRouter

router = APIRouter()


@router.get("/product", tags=["product"])
async def get_products():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]