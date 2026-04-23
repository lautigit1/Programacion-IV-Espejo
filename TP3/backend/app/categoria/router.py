"""
Router de Categorías — expone los endpoints CRUD.
"""

from fastapi import APIRouter, HTTPException, status
from app.categoria.schema import CategoriaCreate, CategoriaUpdate, CategoriaResponse
from app.categoria import service

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("/", response_model=list[CategoriaResponse])
def listar():
    return service.listar_categorias()


@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear(datos: CategoriaCreate):
    return service.crear_categoria(datos)


@router.put("/{id}", response_model=CategoriaResponse)
def actualizar(id: int, datos: CategoriaUpdate):
    resultado = service.actualizar_categoria(id, datos)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return resultado


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int):
    eliminado = service.eliminar_categoria(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
