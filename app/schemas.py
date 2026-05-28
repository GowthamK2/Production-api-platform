from pydantic import BaseModel
from pydantic import Field


class ProductCreate(BaseModel):

    name: str = Field(min_length=2)

    price: float = Field(gt=0)

    stock: int = Field(ge=0)


class ProductResponse(ProductCreate):

    id: int

    class Config:

        from_attributes = True