from fastapi import APIRouter

router = APIRouter()


@router.get("/variant", tags=[""])
async def get_variant():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.post("/variant", tags=["variant"])
async def add_variant():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/variant", tags=["variant"])
async def edit_variant():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/variant", tags=["variant"])
async def delete_item():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

