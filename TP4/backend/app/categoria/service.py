from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate, CategoriaResponse
import app.core.database as db


def _to_response(categoria: Categoria) -> CategoriaResponse:
    return CategoriaResponse(
        id=categoria.id,
        nombre=categoria.nombre,
        descripcion=categoria.descripcion,
    )


def get_all() -> list[CategoriaResponse]:
    return [_to_response(c) for c in db.categorias]


def get_by_id(categoria_id: int) -> CategoriaResponse | None:
    categoria = next((c for c in db.categorias if c.id == categoria_id), None)
    return _to_response(categoria) if categoria else None


def create(data: CategoriaCreate) -> CategoriaResponse:
    global db
    nueva = Categoria(
        id=db.categoria_id_counter,
        nombre=data.nombre,
        descripcion=data.descripcion,
    )
    db.categorias.append(nueva)
    db.categoria_id_counter += 1
    return _to_response(nueva)


def update(categoria_id: int, data: CategoriaUpdate) -> CategoriaResponse | None:
    for i, c in enumerate(db.categorias):
        if c.id == categoria_id:
            db.categorias[i] = Categoria(
                id=c.id,
                nombre=data.nombre,
                descripcion=data.descripcion,
            )
            return _to_response(db.categorias[i])
    return None


def delete(categoria_id: int) -> bool:
    for i, c in enumerate(db.categorias):
        if c.id == categoria_id:
            db.categorias.pop(i)
            return True
    return False
