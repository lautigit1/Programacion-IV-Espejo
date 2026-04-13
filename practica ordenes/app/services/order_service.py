from typing import Tuple, List
from fastapi import HTTPException
from app.database.unit_of_work import UnitOfWork
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate, OrderPagination, OrderRead
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from sqlalchemy.orm import selectinload

class OrderService:
    def create_order(self, order_data: OrderCreate) -> OrderRead:
        with UnitOfWork() as uow:
            product_repo = ProductRepository(uow.session)
            order_repo = OrderRepository(uow.session)
            
            total_amount = 0.0
            order_items = []
            
            # Recorremos los items para validar productos y calcular el total
            for item in order_data.items:
                product = product_repo.get_by_id(item.product_id)
                if not product:
                    raise HTTPException(status_code=404, detail=f"El producto {item.product_id} no existe")
                
                unit_price = product.price
                total_amount += unit_price * item.quantity
                
                order_items.append(OrderItem(
                    product=product,
                    quantity=item.quantity,
                    unit_price=unit_price
                ))
            
            # Armamos la orden final
            order = Order(
                user_email=order_data.user_email,
                total_amount=total_amount,
                items=order_items
            )
            
            # Guardamos todo junto en la misma transaccion
            created_order = order_repo.create(order)
            uow.commit()
            uow.session.refresh(created_order)
            
            return OrderRead.model_validate(created_order)

    def get_order(self, order_id: int) -> OrderRead:
        with UnitOfWork() as uow:
            repo = OrderRepository(uow.session)
            order = repo.get_order_with_items(order_id)
            if not order:
                raise HTTPException(status_code=404, detail="La orden que buscas no existe")
            return OrderRead.model_validate(order)

    def list_orders(self, offset: int, limit: int) -> OrderPagination:
        with UnitOfWork() as uow:
            repo = OrderRepository(uow.session)
            total, orders = repo.list_orders_with_items(offset, limit)
            
            orders_read = [OrderRead.model_validate(o) for o in orders]
            return OrderPagination(total=total, data=orders_read)
