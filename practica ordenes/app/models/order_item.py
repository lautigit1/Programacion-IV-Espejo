from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class OrderItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key='order.id')
    product_id: int = Field(foreign_key='product.id')
    quantity: int = Field(gt=0)
    unit_price: float
    
    order: Optional['Order'] = Relationship(back_populates='items')
    product: Optional['Product'] = Relationship(back_populates='order_items')
