from app.producto.model import Producto, ProductoCategoria
from app.producto.schema import ProductoCreate, ProductoUpdate, ProductoResponse
import app.core.database as db

# Relaciones producto-categoria (en memoria)
relaciones: list[ProductoCategoria] = []


def _to_response(producto: Producto) -> ProductoResponse:
    return ProductoResponse(
        id=producto.id,
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio_base=producto.precio_base,
        imagen_url=producto.imagen_url,
        disponible=producto.disponible,
    )


def get_all() -> list[ProductoResponse]:
    return [_to_response(p) for p in db.productos]


def get_by_id(producto_id: int) -> ProductoResponse | None:
    producto = next((p for p in db.productos if p.id == producto_id), None)
    return _to_response(producto) if producto else None


def create(data: ProductoCreate) -> ProductoResponse:
    nuevo = Producto(
        id=db.producto_id_counter,
        nombre=data.nombre,
        descripcion=data.descripcion,
        precio_base=data.precio_base,
        imagen_url=data.imagen_url,
        disponible=data.disponible,
    )
    db.productos.append(nuevo)
    db.producto_id_counter += 1
    return _to_response(nuevo)


def update(producto_id: int, data: ProductoUpdate) -> ProductoResponse | None:
    for i, p in enumerate(db.productos):
        if p.id == producto_id:
            db.productos[i] = Producto(
                id=p.id,
                nombre=data.nombre,
                descripcion=data.descripcion,
                precio_base=data.precio_base,
                imagen_url=data.imagen_url,
                disponible=data.disponible,
            )
            return _to_response(db.productos[i])
    return None


def delete(producto_id: int) -> bool:
    for i, p in enumerate(db.productos):
        if p.id == producto_id:
            db.productos.pop(i)
            # Limpiar relaciones huérfanas
            relaciones[:] = [r for r in relaciones if r.producto_id != producto_id]
            return True
    return False


# ── ProductoCategoria ─────────────────────────────────────────────────────────

def link_categoria(producto_id: int, categoria_id: int) -> bool:
    """Vincula una categoría a un producto. Ignora duplicados."""
    producto = next((p for p in db.productos if p.id == producto_id), None)
    if not producto:
        return False
    ya_existe = any(
        r.producto_id == producto_id and r.categoria_id == categoria_id
        for r in relaciones
    )
    if not ya_existe:
        relaciones.append(ProductoCategoria(producto_id=producto_id, categoria_id=categoria_id))
    return True


def unlink_categoria(producto_id: int, categoria_id: int) -> bool:
    """Desvincula una categoría de un producto."""
    for i, r in enumerate(relaciones):
        if r.producto_id == producto_id and r.categoria_id == categoria_id:
            relaciones.pop(i)
            return True
    return False


def get_categorias_de_producto(producto_id: int) -> list[int]:
    return [r.categoria_id for r in relaciones if r.producto_id == producto_id]
