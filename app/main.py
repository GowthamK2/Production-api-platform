from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# -----------------------------
# PRODUCT MODEL
# -----------------------------

class Product(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=50
    )

    price: float = Field(gt=0)

    stock: int = Field(ge=0)

    description: Optional[str] = None


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

    if product_id >= len(products_db):

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products_db[product_id]


# -----------------------------
# CREATE PRODUCT
# -----------------------------

@app.post("/products")
def create_product(product: Product):

    products_db.append(product.model_dump())

    return {
        "message": "Product added",
        "data": product
    }


# -----------------------------
# UPDATE PRODUCT
# -----------------------------

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    if product_id >= len(products_db):

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    products_db[product_id] = product.model_dump()

    return {
        "message": "Product updated",
        "data": product
    }


# -----------------------------
# DELETE PRODUCT
# -----------------------------

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id >= len(products_db):

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products_db.pop(product_id)

    return {
        "message": "Product deleted",
        "data": deleted_product
    }