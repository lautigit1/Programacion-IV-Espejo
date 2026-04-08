from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated


CodigoCategoria = Annotated[
    str,
    StringConstraints(pattern=r"^[A-Z]{3}-\d{2}$"),
]


class CategoriaBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    codigo: CodigoCategoria
    descripcion: str = Field(default="", max_length=255)


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaRead(CategoriaBase):
    id: int
    activo: bool
