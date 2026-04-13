from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
