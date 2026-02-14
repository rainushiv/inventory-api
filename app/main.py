from fastapi import FastAPI
from routers import product

app = FastAPI(
    title="InventoryBackend"
)

app.include_router(product.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}