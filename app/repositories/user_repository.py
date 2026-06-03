from sqlalchemy.orm import Session
from app.models import Product

def create_product(
        db: Session,
        product
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

def get_products(
        db: Session
):
    return db.query(Product).all()

def get_product(
        db: Session,
        product_id: int
):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product(
        db: Session,
        product_id: int
):
    return db.query(Product).filter(Product.id == product_id).firstt()

    if Product is None:
        return None
    
    db.delete(Product)
    db.commit()

    return True

