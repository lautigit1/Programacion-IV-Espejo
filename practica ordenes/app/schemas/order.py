from typing import List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from app.schemas.product import ProductRead

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderCreate(BaseModel):
    user_email: EmailStr
    items: List[OrderItemCreate] = Field(min_length=1)

class OrderItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product: ProductRead
    quantity: int
    unit_price: float

class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_email: EmailStr
    total_amount: float
    created_at: datetime
    items: List[OrderItemRead]

class OrderPagination(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    total: int
    data: List[OrderRead]
