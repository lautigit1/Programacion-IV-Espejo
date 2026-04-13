from typing import List
from fastapi import APIRouter
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import ProductService

router = APIRouter(prefix='/products', tags=['Productos'])
product_service = ProductService()

@router.post('', response_model=ProductRead)
def create_product(product: ProductCreate):
    return product_service.create_product(product)

@router.get('', response_model=List[ProductRead])
def list_products():
    return product_service.list_products()
