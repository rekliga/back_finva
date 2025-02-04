from fastapi import APIRouter
from app.api.endpoints import catalogos, formularios

api_router = APIRouter()

# rutas de las entidades
api_router.include_router(catalogos.router, prefix="/catalogos", tags=["Catalogos"])
api_router.include_router(formularios.router, prefix="/users", tags=["Usuarios"])