from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int 
    skills : list[str]

class Product(BaseModel):
    name: str
    price: float
    stock: int 

@app.get("/") 
def home():
    return {"message": "Home route"}

@app.get("/about")
def about():
    return {"message": "About route"}



@app.get("/contact")
def contact():
    return {
        "name": "Gowtham",

        "role": "AI Backend Developer"
    }

@app.get("/Skills")
def skills():
    return {
        "skills": ["FastAPI", "Python"]
    }

@app.get("/projects")
def projects():
    return  {
        "projects": ["Production API Platform", "AI Chatbot"]
    }

@app.get("/products")
def products():
    return {
        "products": ["Laptop", "Keyboard"]
    }

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
    }

@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product Created",
        "data": product 
    }

