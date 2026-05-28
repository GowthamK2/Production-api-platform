from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate


def create_product_service(
    db: Session,
    product: ProductCreate
):

    new_product = Product(

        name=product.name,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product

def get_products_service(
    db: Session
):

    return db.query(Product).all()

def get_product_service(
    db: Session,
    product_id: int
):

    return db.query(Product).filter(
        Product.id == product_id
    ).first()

def delete_product_service(
    db: Session,
    product_id: int
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:

        return None

    db.delete(product)

    db.commit()

    return True