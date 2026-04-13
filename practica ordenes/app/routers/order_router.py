from fastapi import APIRouter, Query
from app.schemas.order import OrderCreate, OrderRead, OrderPagination
from app.services.order_service import OrderService

router = APIRouter(prefix='/orders', tags=['Ordenes'])
order_service = OrderService()

@router.post('', response_model=OrderRead)
def create_order(order: OrderCreate):
    return order_service.create_order(order)

@router.get('/{order_id}', response_model=OrderRead)
def get_order(order_id: int):
    return order_service.get_order(order_id)

@router.get('', response_model=OrderPagination)
def list_orders(offset: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100)):
    return order_service.list_orders(offset, limit)
