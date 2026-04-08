from fastapi import FastAPI

from app.modules.categoria.routers import router as categoria_router
from app.modules.producto.routers import router as producto_router


app = FastAPI(
    title="API Profesional - Gestion de Inventario",
    description="API modular con FastAPI para categorias y productos con validaciones y borrado logico.",
)

app.include_router(categoria_router)
app.include_router(producto_router)
