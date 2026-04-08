from pydantic import BaseModel, Field


class ProductoBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=120)
    descripcion: str = Field(default="", max_length=255)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    stock_minimo: int = Field(ge=0)
    categoria_id: int = Field(gt=0)


class ProductoCreate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id: int
    activo: bool


class ProductoStockResponse(BaseModel):
    id: int
    stock_actual: int
    bajo_stock_minimo: bool
