from typing import List
from sqlmodel import SQLModel, Field, Relationship

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: float
    
    order_items: List['OrderItem'] = Relationship(back_populates='product')
