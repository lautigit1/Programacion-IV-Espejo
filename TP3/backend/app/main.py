"""
Punto de entrada de la aplicación FastAPI.
Configura CORS y registra los routers de cada dominio.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router

app = FastAPI(
    title="TP3 - Categorías y Productos",
    version="1.0.0",
    description="CRUD de Categorías y Productos con FastAPI",
)

# ──────────────────────────────────────────────
# CORS — permite peticiones desde el frontend
# ──────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────
# Routers
# ──────────────────────────────────────────────
app.include_router(categoria_router)
app.include_router(producto_router)


@app.get("/", tags=["Health"])
def health():
    return {"status": "ok", "app": "TP3 - Categorías y Productos"}
