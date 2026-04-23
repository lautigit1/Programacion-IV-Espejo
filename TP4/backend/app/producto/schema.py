from pydantic import BaseModel


class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str] = []
    disponible: bool = True


class ProductoUpdate(BaseModel):
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str] = []
    disponible: bool


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str]
    disponible: bool


class ProductoCategoriaLink(BaseModel):
    categoria_id: int
