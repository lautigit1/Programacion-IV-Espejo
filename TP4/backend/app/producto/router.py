from fastapi import APIRouter, HTTPException, status
from app.producto.schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse,
    ProductoCategoriaLink,
)
from app.producto import service

router = APIRouter(prefix="/productos", tags=["productos"])


# ── Productos ─────────────────────────────────────────────────────────────────

@router.get("/", response_model=list[ProductoResponse])
def listar_productos() -> list[ProductoResponse]:
    return service.get_all()


@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int) -> ProductoResponse:
    producto = service.get_by_id(producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )
    return producto


@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate) -> ProductoResponse:
    return service.create(data)


@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, data: ProductoUpdate) -> ProductoResponse:
    producto = service.update(producto_id, data)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )
    return producto


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int) -> None:
    eliminado = service.delete(producto_id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )


# ── ProductoCategoria ─────────────────────────────────────────────────────────

@router.get("/{producto_id}/categorias", response_model=list[int])
def listar_categorias_de_producto(producto_id: int) -> list[int]:
    producto = service.get_by_id(producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )
    return service.get_categorias_de_producto(producto_id)


@router.post("/{producto_id}/categorias", status_code=status.HTTP_201_CREATED)
def vincular_categoria(producto_id: int, data: ProductoCategoriaLink) -> dict[str, str]:
    vinculado = service.link_categoria(producto_id, data.categoria_id)
    if not vinculado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )
    return {"message": f"Categoría {data.categoria_id} vinculada al producto {producto_id}"}


@router.delete("/{producto_id}/categorias/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def desvincular_categoria(producto_id: int, categoria_id: int) -> None:
    desvinculado = service.unlink_categoria(producto_id, categoria_id)
    if not desvinculado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relación no encontrada",
        )
