from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class User(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    name: str
    price: float
    stock: int

list = [
    Product(name="Apple", price=30.0, stock=10),
    Product(name="Banana", price=20.0, stock=20),
    Product(name="Strawberry", price=10.0, stock=30),
    Product(name="Orange", price=10.0, stock=40),
]

@app.post("/api/v1/user")
async def login(user: User):
    if user.username == "admin" and user.password == "admin":
        return {"message": "Login Success"}
    return {"message": "user or password incorrect"}

@app.get("/api/v1/product")
async def login():
    return {"products": list,"count": len(list)}

@app.get("/shoppingcart/{id}")
async def index(id:int):
    return {"message": "Hello World"}