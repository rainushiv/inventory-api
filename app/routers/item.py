from fastapi import APIRouter

router = APIRouter()


@router.get("/item", tags=["item"])
async def get_item():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.post("/item", tags=["item"])
async def add_item():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/item", tags=["item"])
async def edit_item():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/item", tags=["item"])
async def delete_item():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

