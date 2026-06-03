from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    price = Column(Float)

    stock = Column(Integer)

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True 
    )

    username = Column(
        String,
        unique=True,
        nullable=False
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )


