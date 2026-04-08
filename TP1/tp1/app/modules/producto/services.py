from app.modules.producto.schemas import ProductoCreate


db_productos: list[dict] = []
_producto_id_actual: int = 0


def crear_producto(producto_data: ProductoCreate) -> dict:
    global _producto_id_actual
    _producto_id_actual += 1
    nuevo_producto = {
        "id": _producto_id_actual,
        "activo": True,
        **producto_data.model_dump(),
    }
    db_productos.append(nuevo_producto)
    return nuevo_producto


def obtener_productos(skip: int = 0, limit: int = 10) -> list[dict]:
    return db_productos[skip : skip + limit]


def obtener_producto_por_id(producto_id: int) -> dict | None:
    for producto in db_productos:
        if producto["id"] == producto_id:
            return producto
    return None


def actualizar_producto(producto_id: int, producto_data: ProductoCreate) -> dict | None:
    for indice, producto in enumerate(db_productos):
        if producto["id"] == producto_id:
            producto_actualizado = {
                "id": producto_id,
                "activo": producto["activo"],
                **producto_data.model_dump(),
            }
            db_productos[indice] = producto_actualizado
            return producto_actualizado
    return None


def desactivar_producto(producto_id: int) -> dict | None:
    producto = obtener_producto_por_id(producto_id)
    if producto is None:
        return None
    producto["activo"] = False
    return producto


def obtener_estado_stock(producto_id: int) -> dict | None:
    producto = obtener_producto_por_id(producto_id)
    if producto is None:
        return None
    stock_actual = producto["stock"]
    return {
        "id": producto["id"],
        "stock_actual": stock_actual,
        "bajo_stock_minimo": stock_actual < producto["stock_minimo"],
    }
