from fastapi import APIRouter, HTTPException, status
from app.categoria.schema import CategoriaCreate, CategoriaUpdate, CategoriaResponse
from app.categoria import service

router = APIRouter(prefix="/categorias", tags=["categorias"])


@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias() -> list[CategoriaResponse]:
    return service.get_all()


@router.get("/{categoria_id}", response_model=CategoriaResponse)
def obtener_categoria(categoria_id: int) -> CategoriaResponse:
    categoria = service.get_by_id(categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con id {categoria_id} no encontrada",
        )
    return categoria


@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear_categoria(data: CategoriaCreate) -> CategoriaResponse:
    return service.create(data)


@router.put("/{categoria_id}", response_model=CategoriaResponse)
def actualizar_categoria(categoria_id: int, data: CategoriaUpdate) -> CategoriaResponse:
    categoria = service.update(categoria_id, data)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con id {categoria_id} no encontrada",
        )
    return categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(categoria_id: int) -> None:
    eliminada = service.delete(categoria_id)
    if not eliminada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con id {categoria_id} no encontrada",
        )
