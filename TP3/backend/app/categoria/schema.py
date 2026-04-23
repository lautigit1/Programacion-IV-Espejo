from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nombre: str
    descripcion: str


class CategoriaUpdate(BaseModel):
    nombre: str
    descripcion: str


class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
