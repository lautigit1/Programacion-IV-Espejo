from fastapi import HTTPException, status

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate


class ProductService:
    """Reglas de negocio y orquestación entre repositorio y respuestas API."""

    def __init__(self, repository: ProductRepository) -> None:
        self._repo = repository

    def _ensure_found(self, product_id: int) -> Product:
        entity = self._repo.get_by_id(product_id)
        if entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"mensaje": "Producto no encontrado", "id": product_id},
            )
        return entity

    def _validate_business_create(self, data: ProductCreate) -> None:
        """
        Validaciones de negocio (además de Pydantic).
        Aquí van reglas que dependan del dominio y no solo del formato.
        """
        if data.precio <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"mensaje": "El precio debe ser mayor que cero."},
            )
        if data.stock < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"mensaje": "El stock no puede ser negativo."},
            )

    def _validate_business_update(self, data: ProductUpdate) -> None:
        payload = data.model_dump(exclude_unset=True)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "mensaje": "Debe enviar al menos un campo para actualizar el producto."
                },
            )
        if "precio" in payload and payload["precio"] is not None and payload["precio"] <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"mensaje": "El precio debe ser mayor que cero."},
            )
        if "stock" in payload and payload["stock"] is not None and payload["stock"] < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"mensaje": "El stock no puede ser negativo."},
            )

    def create_product(self, data: ProductCreate) -> ProductRead:
        self._validate_business_create(data)
        entity = Product(
            nombre=data.nombre,
            descripcion=data.descripcion,
            precio=data.precio,
            stock=data.stock,
        )
        saved = self._repo.create(entity)
        return ProductRead.model_validate(saved)

    def list_products(self) -> list[ProductRead]:
        items = self._repo.list_all()
        return [ProductRead.model_validate(p) for p in items]

    def get_product(self, product_id: int) -> ProductRead:
        entity = self._ensure_found(product_id)
        return ProductRead.model_validate(entity)

    def update_product(self, product_id: int, data: ProductUpdate) -> ProductRead:
        self._validate_business_update(data)
        entity = self._ensure_found(product_id)
        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(entity, field, value)
        saved = self._repo.update(entity)
        return ProductRead.model_validate(saved)

    def delete_product(self, product_id: int) -> None:
        entity = self._ensure_found(product_id)
        self._repo.delete(entity)
