"""
Lógica de negocio para Categorías.
Opera sobre el store en memoria definido en core/database.py.
"""

from app.core import database
from app.categoria.model import CategoriaInterna
from app.categoria.schema import CategoriaCreate, CategoriaUpdate, CategoriaResponse


def listar_categorias() -> list[CategoriaResponse]:
    return [
        CategoriaResponse(id=c.id, nombre=c.nombre, descripcion=c.descripcion)
        for c in database.categorias
    ]


def crear_categoria(datos: CategoriaCreate) -> CategoriaResponse:
    nueva = CategoriaInterna(
        id=database.next_categoria_id(),
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )
    database.categorias.append(nueva)
    return CategoriaResponse(id=nueva.id, nombre=nueva.nombre, descripcion=nueva.descripcion)


def actualizar_categoria(id: int, datos: CategoriaUpdate) -> CategoriaResponse | None:
    for cat in database.categorias:
        if cat.id == id:
            cat.nombre = datos.nombre
            cat.descripcion = datos.descripcion
            return CategoriaResponse(id=cat.id, nombre=cat.nombre, descripcion=cat.descripcion)
    return None


def eliminar_categoria(id: int) -> bool:
    for i, cat in enumerate(database.categorias):
        if cat.id == id:
            database.categorias.pop(i)
            return True
    return False
