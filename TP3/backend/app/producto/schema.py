from pydantic import BaseModel


class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str]
    disponible: bool


class ProductoUpdate(BaseModel):
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str]
    disponible: bool


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str]
    disponible: bool


class ProductoCategoriaCreate(BaseModel):
    producto_id: int
    categoria_id: int
