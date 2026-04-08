from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Productos"])


def get_product_service(
    session: Annotated[Session, Depends(get_session)],
) -> ProductService:
    return ProductService(ProductRepository(session))


@router.post(
    "",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear producto",
)
def crear_producto(
    payload: ProductCreate,
    service: Annotated[ProductService, Depends(get_product_service)],
) -> ProductRead:
    """Registra un producto nuevo y devuelve el recurso con su id asignado."""
    return service.create_product(payload)


@router.get(
    "",
    response_model=list[ProductRead],
    summary="Listar productos",
)
def listar_productos(
    service: Annotated[ProductService, Depends(get_product_service)],
) -> list[ProductRead]:
    """Devuelve todos los productos ordenados por id."""
    return service.list_products()


@router.get(
    "/{product_id}",
    response_model=ProductRead,
    summary="Obtener producto por id",
)
def obtener_producto(
    product_id: int,
    service: Annotated[ProductService, Depends(get_product_service)],
) -> ProductRead:
    """Devuelve un producto o 404 si no existe."""
    return service.get_product(product_id)


@router.put(
    "/{product_id}",
    response_model=ProductRead,
    summary="Actualizar producto",
)
def actualizar_producto(
    product_id: int,
    payload: ProductUpdate,
    service: Annotated[ProductService, Depends(get_product_service)],
) -> ProductRead:
    """Actualización parcial: solo se modifican los campos enviados."""
    return service.update_product(product_id, payload)


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    summary="Eliminar producto",
)
def eliminar_producto(
    product_id: int,
    service: Annotated[ProductService, Depends(get_product_service)],
) -> None:
    """Elimina el producto. Respuesta vacía (204) si tuvo éxito."""
    service.delete_product(product_id)
