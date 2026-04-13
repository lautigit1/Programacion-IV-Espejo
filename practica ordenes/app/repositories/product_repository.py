from sqlmodel import Session, select
from typing import List
from app.models.product import Product

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, product: Product) -> Product:
        self.session.add(product)
        self.session.flush()
        self.session.refresh(product)
        return product

    def get_by_id(self, product_id: int) -> Product | None:
        return self.session.get(Product, product_id)

    def get_all(self) -> List[Product]:
        statement = select(Product)
        return list(self.session.exec(statement).all())
