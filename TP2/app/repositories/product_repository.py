from collections.abc import Sequence
from typing import Optional

from sqlmodel import Session, select

from app.models.product import Product


class ProductRepository:
    """Acceso a datos: consultas y persistencia sin lógica de negocio."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, product: Product) -> Product:
        self._session.add(product)
        self._session.commit()
        self._session.refresh(product)
        return product

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self._session.get(Product, product_id)

    def list_all(self) -> Sequence[Product]:
        statement = select(Product).order_by(Product.id)
        return self._session.exec(statement).all()

    def update(self, product: Product) -> Product:
        self._session.add(product)
        self._session.commit()
        self._session.refresh(product)
        return product

    def delete(self, product: Product) -> None:
        self._session.delete(product)
        self._session.commit()
