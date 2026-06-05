from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ProductCreate
from app.schemas import ProductResponse
from app.models import Product

from app.services import (
    create_product_service,
    get_products_service,
    get_product_service,
    delete_product_service
)

router = APIRouter(
prefix="/products",
tags=["Products"]
)

@router.post("", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product_service(
db,
product
)

@router.get("", response_model=list[ProductResponse])
async def get_products(
    db: Session = Depends(get_db)
):
    return get_products_service(db)

@router.get("/{product_id}", response_model=ProductResponse)
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


@router.put("/{product_id}")
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

@router.delete("/{product_id}")
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

