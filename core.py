from fastapi import FastAPI
from auth import clone
from cargo import eats
from store import users

app = FastAPI()
app.include_router(clone)
app.include_router(eats)
app.include_router(users)

@app.get("/")
async def root():
    return {"Hello": "Hello World"}