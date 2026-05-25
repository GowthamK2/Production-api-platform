from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services import (
    get_all_products,
    get_single_product,
    create_new_product,
    update_existing_product,
    delete_existing_product
)

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

    products = get_all_products()

    return {
        "products": products
    }


# -----------------------------
# GET SINGLE PRODUCT
# -----------------------------

@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = get_single_product(product_id)

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# -----------------------------
# CREATE PRODUCT
# -----------------------------

@app.post("/products")
def create_product(product: Product):

    created_product = create_new_product(product)

    return {
        "message": "Product added",
        "data": created_product
    }


# -----------------------------
# UPDATE PRODUCT
# -----------------------------

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    updated_product = update_existing_product(
        product_id,
        product
    )

    if updated_product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product updated",
        "data": updated_product
    }


# -----------------------------
# DELETE PRODUCT
# -----------------------------

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    deleted_product = delete_existing_product(product_id)

    if deleted_product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted",
        "data": deleted_product
    }