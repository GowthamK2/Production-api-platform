from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict

model_config = ConfigDict(
    from_attributes=True
)


class ProductCreate(BaseModel):

    name: str = Field(min_length=2)

    price: float = Field(gt=0)

    stock: int = Field(ge=0)


class ProductResponse(ProductCreate):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )

class UserCreate(BaseModel):
    username: str
    email: str
    password: str 

class UserLogin(BaseModel):
    username: str
    password: str