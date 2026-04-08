from app.modules.categoria.schemas import CategoriaCreate


db_categorias: list[dict] = []
_categoria_id_actual: int = 0


def crear_categoria(categoria_data: CategoriaCreate) -> dict:
    global _categoria_id_actual
    _categoria_id_actual += 1
    nueva_categoria = {
        "id": _categoria_id_actual,
        "activo": True,
        **categoria_data.model_dump(),
    }
    db_categorias.append(nueva_categoria)
    return nueva_categoria


def obtener_categorias(skip: int = 0, limit: int = 10) -> list[dict]:
    return db_categorias[skip : skip + limit]


def obtener_categoria_por_id(categoria_id: int) -> dict | None:
    for categoria in db_categorias:
        if categoria["id"] == categoria_id:
            return categoria
    return None


def actualizar_categoria(categoria_id: int, categoria_data: CategoriaCreate) -> dict | None:
    for indice, categoria in enumerate(db_categorias):
        if categoria["id"] == categoria_id:
            categoria_actualizada = {
                "id": categoria_id,
                "activo": categoria["activo"],
                **categoria_data.model_dump(),
            }
            db_categorias[indice] = categoria_actualizada
            return categoria_actualizada
    return None


def desactivar_categoria(categoria_id: int) -> dict | None:
    categoria = obtener_categoria_por_id(categoria_id)
    if categoria is None:
        return None
    categoria["activo"] = False
    return categoria
