"""
Lógica de negocio para Productos y relación Producto-Categoría.
"""

from app.core import database
from app.producto.model import ProductoInterno
from app.producto.schema import (
    ProductoCreate,
    ProductoUpdate,
    ProductoResponse,
    ProductoCategoriaCreate,
)


def listar_productos() -> list[ProductoResponse]:
    return [
        ProductoResponse(
            id=p.id,
            nombre=p.nombre,
            descripcion=p.descripcion,
            precio_base=p.precio_base,
            imagen_url=p.imagen_url,
            disponible=p.disponible,
        )
        for p in database.productos
    ]


def crear_producto(datos: ProductoCreate) -> ProductoResponse:
    nuevo = ProductoInterno(
        id=database.next_producto_id(),
        nombre=datos.nombre,
        descripcion=datos.descripcion,
        precio_base=datos.precio_base,
        imagen_url=datos.imagen_url,
        disponible=datos.disponible,
    )
    database.productos.append(nuevo)
    return ProductoResponse(
        id=nuevo.id,
        nombre=nuevo.nombre,
        descripcion=nuevo.descripcion,
        precio_base=nuevo.precio_base,
        imagen_url=nuevo.imagen_url,
        disponible=nuevo.disponible,
    )


def actualizar_producto(id: int, datos: ProductoUpdate) -> ProductoResponse | None:
    for prod in database.productos:
        if prod.id == id:
            prod.nombre = datos.nombre
            prod.descripcion = datos.descripcion
            prod.precio_base = datos.precio_base
            prod.imagen_url = datos.imagen_url
            prod.disponible = datos.disponible
            return ProductoResponse(
                id=prod.id,
                nombre=prod.nombre,
                descripcion=prod.descripcion,
                precio_base=prod.precio_base,
                imagen_url=prod.imagen_url,
                disponible=prod.disponible,
            )
    return None


def eliminar_producto(id: int) -> bool:
    for i, prod in enumerate(database.productos):
        if prod.id == id:
            database.productos.pop(i)
            # Limpiar relaciones huérfanas
            database.producto_categoria[:] = [
                r for r in database.producto_categoria if r["producto_id"] != id
            ]
            return True
    return False


# ──────────────────────────────────────────────
# Relación Producto-Categoría
# ──────────────────────────────────────────────

def asociar_categoria(datos: ProductoCategoriaCreate) -> dict[str, int]:
    relacion = {"producto_id": datos.producto_id, "categoria_id": datos.categoria_id}
    # Evitar duplicados
    if relacion not in database.producto_categoria:
        database.producto_categoria.append(relacion)
    return relacion


def listar_relaciones() -> list[dict[str, int]]:
    return list(database.producto_categoria)
