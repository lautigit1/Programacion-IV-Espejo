from dataclasses import dataclass, field


@dataclass
class ProductoInterno:
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str]
    disponible: bool
