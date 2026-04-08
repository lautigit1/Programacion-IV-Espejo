from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProductBase(BaseModel):
    """Campos comunes y reglas de validación a nivel de esquema (Pydantic)."""

    nombre: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Nombre obligatorio, sin quedar vacío tras normalizar.",
    )
    descripcion: str = Field(default="", max_length=2000)
    precio: float = Field(..., gt=0, description="Precio estrictamente mayor que cero.")
    stock: int = Field(default=0, ge=0, description="Stock no negativo.")

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str) -> str:
        s = v.strip()
        if not s:
            raise ValueError("El nombre es obligatorio.")
        return s

    @field_validator("descripcion")
    @classmethod
    def descripcion_normalizada(cls, v: str) -> str:
        return v.strip() if v else ""


class ProductCreate(ProductBase):
    """Payload para crear un producto (validación de entrada)."""

    pass


class ProductUpdate(BaseModel):
    """Actualización parcial: solo se modifican campos enviados."""

    model_config = ConfigDict(extra="forbid")

    nombre: Optional[str] = Field(default=None, min_length=1, max_length=255)
    descripcion: Optional[str] = Field(default=None, max_length=2000)
    precio: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)

    @field_validator("nombre")
    @classmethod
    def nombre_si_presente(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        s = v.strip()
        if not s:
            raise ValueError("El nombre no puede estar vacío.")
        return s

    @field_validator("descripcion")
    @classmethod
    def descripcion_si_presente(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return v.strip()


class ProductRead(ProductBase):
    """Respuesta al cliente: incluye id generado por la base de datos."""

    model_config = ConfigDict(from_attributes=True)

    id: int
