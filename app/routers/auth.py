from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db

from app.models import User

from app.schemas import UserCreate
from app.schemas import UserLogin

from app.services import create_user
from app.services import login_user

from app.security import verify_token
from app.security import verify_password
from app.security import create_access_token

router = APIRouter(
tags=["Authentication"]
)




from fastapi.security import OAuth2PasswordBearer


router = APIRouter(
    tags=["Authentication"]
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)

@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(user, db)

@router.post("/login")
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


@router.get("/profile")
def profile(
    current_user: str = Depends(
        get_current_user
    )
):
    return {
        "username": current_user

    }


@router.post("/token")
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