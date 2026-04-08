from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers.products import router as products_router

app = FastAPI(
    title="Gestor de Productos",
    description=(
        "API REST para administrar productos con PostgreSQL, SQLModel y capas "
        "(router, service, repository)."
    ),
    version="1.0.0",
)


@app.exception_handler(RequestValidationError)
async def validacion_a_400(_request, exc: RequestValidationError) -> JSONResponse:
    """
    Los errores de Pydantic suelen devolver 422; el enunciado pide 400 para datos inválidos.
    """
    return JSONResponse(
        status_code=400,
        content={
            "mensaje": "Los datos enviados no son válidos.",
            "errores": exc.errors(),
        },
    )


@app.get("/", tags=["Raíz"])
def raiz() -> dict[str, str]:
    return {
        "mensaje": "Gestor de Productos API",
        "documentacion_interactiva": "/docs",
        "documentacion_alternativa": "/redoc",
    }


app.include_router(products_router)
