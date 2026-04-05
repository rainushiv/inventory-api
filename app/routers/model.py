from fastapi import APIRouter
import logging
router = APIRouter()
logger = logging.getLogger(__name__)
@router.get("/model", tags=["model"])
async def get_models():
    logger.info("This model happened ")
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.post("/model", tags=["model"])
async def add_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

@router.put("/model", tags=["model"])
async def edit_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]


@router.delete("/model", tags=["model"])
async def delete_model():
    return [{"Iphone": "Iphone 13"},{"Samsung": "Samsung S22"}]

