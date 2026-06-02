from app.services import get_products_service
from app.services import get_product_service
from app.services import create_product_service
from app.services import delete_product_service
from app.schemas import ProductResponse 
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends

from fastapi.middleware.cors import CORSMiddleware

import time


from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from app.security import verify_token


from app.database import engine
from app.database import Base
from app.database import get_db

from app.models import Product
from app.models import User

from app.schemas import ProductCreate
from app.schemas import ProductResponse
from app.schemas import UserCreate 
from app.services import create_user 

from app.schemas import UserLogin
from app.services import login_user 
from app.security import verify_password
from app.security import create_access_token

import logging

logging.basicConfig(
    level=logging.INFO 
)

logger = logging.getLogger(__name__)


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"took {process_time:.4f} seconds"
    )

    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)


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

@app.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(user, db)

@app.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    
    result = login_user(
        user,
        db 
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    return result

def get_current_user(
        token: str = Depends(oauth2_scheme)
):
    username = verify_token(token)

    return username 


@app.get("/profile")
def profile(
    current_user: str = Depends(
        get_current_user
    )
):
    return {
        "username": current_user

    }


@app.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }