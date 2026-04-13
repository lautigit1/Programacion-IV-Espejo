from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.session import create_db_and_tables
from app.routers import product_router, order_router
from app.models import product, order, order_item

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title='API de Gestion de Ordenes', lifespan=lifespan)

app.include_router(product_router.router)
app.include_router(order_router.router)

@app.get('/')
def root():
    return {'mensaje': 'La API de Ordenes esta funcionando'}
