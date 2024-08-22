from fastapi import APIRouter

clone = APIRouter(prefix="/home", tags=["home"])

@clone.get("/uy")
async def home():
    return {"Hello": "Assalomu alikum"}

@clone.get("/login")
async def login():
    return {"Hello": "Login page"}

@clone.get("/register")
async def register():
    return {"Hello": "Register page"}

@clone.get("/logout")
async def logout():
    return {"Hello": "Logout page"}

@clone.get("/password_reset")
async def password_reset():
    return {"Hello": "Password reset page"}

@clone.get("/password_configurations")
async def password_configurations():
    return {"Hello": "Password configuration page"}
