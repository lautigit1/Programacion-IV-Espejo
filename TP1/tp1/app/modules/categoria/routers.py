from fastapi import APIRouter, HTTPException, Query, status

from app.modules.categoria.schemas import CategoriaCreate, CategoriaRead
from app.modules.categoria.services import (
    actualizar_categoria,
    crear_categoria,
    desactivar_categoria,
    obtener_categoria_por_id,
    obtener_categorias,
)


router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def alta_categoria(categoria_data: CategoriaCreate) -> dict:
    return crear_categoria(categoria_data)


@router.get("/", response_model=list[CategoriaRead])
def listar_categorias(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
) -> list[dict]:
    return obtener_categorias(skip=skip, limit=limit)


@router.get("/{categoria_id}", response_model=CategoriaRead)
def detalle_categoria(categoria_id: int) -> dict:
    categoria = obtener_categoria_por_id(categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@router.put("/{categoria_id}", response_model=CategoriaRead)
def reemplazar_categoria(categoria_id: int, categoria_data: CategoriaCreate) -> dict:
    categoria = actualizar_categoria(categoria_id, categoria_data)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@router.put("/{categoria_id}/desactivar", response_model=CategoriaRead)
def baja_logica_categoria(categoria_id: int) -> dict:
    categoria = desactivar_categoria(categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria
