from fastapi import APIRouter

users = APIRouter()

@users.get("/users_customer")
async def customer_users():
    return {"Hello": "My customer"}

@users.get("/users_delivery")
async def delivery_users():
    return {"Hello": "My delivery"}

@users.get("/users_employees")
async def employees_users():
    return {"Hello": "My employees"}

@users.get("/admin")
async def admin_users():
    return {"Hello": "My admin"}