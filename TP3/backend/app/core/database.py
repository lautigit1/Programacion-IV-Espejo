"""
Almacenamiento en memoria para categorías y productos.
Funciona como base de datos simple con listas y contadores de ID.
"""

from app.categoria.model import CategoriaInterna
from app.producto.model import ProductoInterno

# ──────────────────────────────────────────────
# Categorías
# ──────────────────────────────────────────────
categorias: list[CategoriaInterna] = []
categoria_id_counter: int = 1


def next_categoria_id() -> int:
    global categoria_id_counter
    id_ = categoria_id_counter
    categoria_id_counter += 1
    return id_


# ──────────────────────────────────────────────
# Productos
# ──────────────────────────────────────────────
productos: list[ProductoInterno] = []
producto_id_counter: int = 1


def next_producto_id() -> int:
    global producto_id_counter
    id_ = producto_id_counter
    producto_id_counter += 1
    return id_


# ──────────────────────────────────────────────
# Relación Producto-Categoría
# ──────────────────────────────────────────────
producto_categoria: list[dict[str, int]] = []
