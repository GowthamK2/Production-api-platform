from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# MODELS
# -----------------------------

class User(BaseModel):
    name: str
    age: int
    skills: list[str]


class Product(BaseModel):
    name: str
    price: float
    stock: int


# -----------------------------
# FAKE DATABASE
# -----------------------------

products_db = []


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Production API Platform Running"
    }


# -----------------------------
# CREATE USER
# -----------------------------

@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created",
        "data": user
    }


# -----------------------------
# CREATE PRODUCT
# -----------------------------

@app.post("/products")
def create_product(product: Product):

    products_db.append(product.dict())

    return {
        "message": "Product added",
        "data": product
    }


# -----------------------------
# GET ALL PRODUCTS
# -----------------------------

@app.get("/products")
def get_products():

    return {
        "products": products_db
    }


# -----------------------------
# GET SINGLE PRODUCT
# -----------------------------

@app.get("/products/{product_id}")
def get_product(product_id: int):

    return products_db[product_id]


# -----------------------------
# UPDATE PRODUCT
# -----------------------------

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    products_db[product_id] = product.dict()

    return {
        "message": "Product updated",
        "updated_product": product
    }


# -----------------------------
# DELETE PRODUCT
# -----------------------------

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    deleted_product = products_db.pop(product_id)

    return {
        "message": "Product deleted",
        "deleted_product": deleted_product
    }