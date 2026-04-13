from typing import List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_email: str = Field(index=True)
    total_amount: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    items: List['OrderItem'] = Relationship(back_populates='order')
