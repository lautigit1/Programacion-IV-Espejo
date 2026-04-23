from dataclasses import dataclass, field


@dataclass
class Producto:
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str] = field(default_factory=list)
    disponible: bool = True


@dataclass
class ProductoCategoria:
    producto_id: int
    categoria_id: int
