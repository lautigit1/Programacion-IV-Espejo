from typing import List
from app.database.unit_of_work import UnitOfWork
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead
from app.repositories.product_repository import ProductRepository
from sqlmodel import Session

class ProductService:
    def create_product(self, product_data: ProductCreate) -> ProductRead:
        with UnitOfWork() as uow:
            repo = ProductRepository(uow.session)
            product = Product(name=product_data.name, price=product_data.price)
            created_product = repo.create(product)
            uow.commit()
            uow.session.refresh(created_product)
            return ProductRead.model_validate(created_product)

    def list_products(self) -> List[ProductRead]:
        with UnitOfWork() as uow:
            repo = ProductRepository(uow.session)
            products = repo.get_all()
            return [ProductRead.model_validate(p) for p in products]
