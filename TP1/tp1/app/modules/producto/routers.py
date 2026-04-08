from fastapi import APIRouter, HTTPException, Query, status

from app.modules.producto.schemas import (
    ProductoCreate,
    ProductoRead,
    ProductoStockResponse,
)
from app.modules.producto.services import (
    actualizar_producto,
    crear_producto,
    desactivar_producto,
    obtener_estado_stock,
    obtener_producto_por_id,
    obtener_productos,
)


router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def alta_producto(producto_data: ProductoCreate) -> dict:
    return crear_producto(producto_data)


@router.get("/", response_model=list[ProductoRead])
def listar_productos(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
) -> list[dict]:
    return obtener_productos(skip=skip, limit=limit)


@router.get("/{producto_id}", response_model=ProductoRead)
def detalle_producto(producto_id: int) -> dict:
    producto = obtener_producto_por_id(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.put("/{producto_id}", response_model=ProductoRead)
def reemplazar_producto(producto_id: int, producto_data: ProductoCreate) -> dict:
    producto = actualizar_producto(producto_id, producto_data)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.put("/{producto_id}/desactivar", response_model=ProductoRead)
def baja_logica_producto(producto_id: int) -> dict:
    producto = desactivar_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.get("/{producto_id}/stock", response_model=ProductoStockResponse)
def estado_stock_producto(producto_id: int) -> dict:
    estado_stock = obtener_estado_stock(producto_id)
    if estado_stock is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return estado_stock
