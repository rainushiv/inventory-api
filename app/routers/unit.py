from fastapi import APIRouter

router = APIRouter()


@router.get("/unit", tags=["unit"])
async def get_unit():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.post("/unit", tags=["unit"])
async def add_unit():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/unit", tags=["unit"])
async def edit_unit():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/unit", tags=["unit"])
async def delete_unit():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


