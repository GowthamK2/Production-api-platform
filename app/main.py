from app.services import get_products_service
from app.services import get_product_service
from app.services import create_product_service
from app.services import delete_product_service
from app.schemas import ProductResponse 
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.database import engine
from app.database import Base

from app.models import Product

from app.schemas import ProductCreate
from app.schemas import ProductResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()


# -----------------------------
# DATABASE SESSION
# -----------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Production API Platform Running"
    }

@app.post("/products", response_model=ProductResponse)

def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product_service(
        db,
        product
    )

# -----------------------------
# GET ALL PRODUCTS
# -----------------------------

@app.get("/products", response_model=list[ProductResponse])

def get_products(
    db: Session = Depends(get_db)
):

    return get_products_service(db)


# -----------------------------
# GET SINGLE PRODUCT
# -----------------------------

@app.get("/products/{product_id}", response_model=ProductResponse)

def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = get_product_service(
        db,
        product_id
    )

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

# -----------------------------
# UPDATE PRODUCT
# -----------------------------

@app.put("/products/{product_id}")

def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.name = updated_product.name
    product.price = updated_product.price
    product.stock = updated_product.stock

    db.commit()

    db.refresh(product)

    return {
        "message": "Product updated",
        "data": product
    }


# -----------------------------
# DELETE PRODUCT
# -----------------------------

@app.delete("/products/{product_id}")

def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_product_service(
        db,
        product_id
    )

    if deleted is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted"
    }