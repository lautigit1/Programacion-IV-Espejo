"""
Router de Productos — expone los endpoints CRUD y la relación Producto-Categoría.
"""

from fastapi import APIRouter, HTTPException, status
from app.producto.schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse,
    ProductoCategoriaCreate,
)
from app.producto import service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoResponse])
def listar():
    return service.listar_productos()


@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear(datos: ProductoCreate):
    return service.crear_producto(datos)


@router.put("/{id}", response_model=ProductoResponse)
def actualizar(id: int, datos: ProductoUpdate):
    resultado = service.actualizar_producto(id, datos)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return resultado


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id: int):
    eliminado = service.eliminar_producto(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")


# ──────────────────────────────────────────────
# Relación Producto-Categoría
# ──────────────────────────────────────────────

@router.post("/categorias", status_code=status.HTTP_201_CREATED)
def asociar_categoria(datos: ProductoCategoriaCreate) -> dict[str, int]:
    return service.asociar_categoria(datos)


@router.get("/categorias", response_model=list[dict[str, int]])
def listar_relaciones():
    return service.listar_relaciones()
