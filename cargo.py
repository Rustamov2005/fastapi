from fastapi import APIRouter

eats = APIRouter(prefix="/eats", tags=["eats"])

@eats.get("/delivery")
async def delivery():
    return {"delivery": "Delivery page"}

@eats.get("/orders")
async def orders():
    return {"orders": "Orders page"}

@eats.get("/orders_story")
async def orders_story():
    return {"orders_story": "Orders story page"}

@eats.get("/products")
async def products():
    return {"products": "Product page"}
