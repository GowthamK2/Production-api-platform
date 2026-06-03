from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate

from app.models import User
from app.security import hash_password 

from app.security import verify_password
from app.security import create_access_token 

from app.repositories.product_repository import create_product

import logging

logger = logging.getLogger(__name__)

def create_product_service(
    db,
    product
):
    return create_product(db, product)

    

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

def create_user(user, db):

   

    hashed_pw = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw 
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    logger.info(
        f"User Registered: {user.username}"
    )

    return {
        "message": "User registered successfully"
    }

def login_user(user, db):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if db_user is None:
        return None

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        return None
    
    token = create_access_token(
        {
            "sub": db_user.username
        }
    )
    logger.info(
        f"User Logged in: {db_user.username}"
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
