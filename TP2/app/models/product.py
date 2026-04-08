from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    """Entidad persistida en PostgreSQL (capa Model / dominio de datos)."""

    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=255, index=True)
    descripcion: str = Field(default="", max_length=2000)
    precio: float
    stock: int = 0
