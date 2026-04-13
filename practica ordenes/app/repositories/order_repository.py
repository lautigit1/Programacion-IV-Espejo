from sqlmodel import Session, select, func
from typing import List, Tuple
from app.models.order import Order
from app.models.order_item import OrderItem
from sqlalchemy.orm import selectinload

class OrderRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, order: Order) -> Order:
        self.session.add(order)
        self.session.flush()
        self.session.refresh(order)
        return order

    def get_by_id(self, order_id: int) -> Order | None:
        return self.session.get(Order, order_id)

    def get_order_with_items(self, order_id: int) -> Order | None:
        statement = select(Order).where(Order.id == order_id).options(
            selectinload(Order.items).selectinload(OrderItem.product)
        )
        return self.session.exec(statement).first()

    def list_orders(self, offset: int, limit: int) -> Tuple[int, List[Order]]:
        total_statement = select(func.count(Order.id))
        total = self.session.exec(total_statement).one()
        
        statement = select(Order).offset(offset).limit(limit)
        orders = list(self.session.exec(statement).all())
        
        return total, orders

    def list_orders_with_items(self, offset: int, limit: int) -> Tuple[int, List[Order]]:
        total_statement = select(func.count(Order.id))
        total = self.session.exec(total_statement).one()
        
        statement = select(Order).offset(offset).limit(limit).options(
            selectinload(Order.items).selectinload(OrderItem.product)
        )
        orders = list(self.session.exec(statement).all())
        
        return total, orders
