from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    description: str
    image: str
    category_pk: int


class ProductCreate(ProductBase):
    pass

