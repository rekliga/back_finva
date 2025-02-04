from fastapi import APIRouter, Depends, HTTPException, Query
from infraestructure.dependencias.containers import Container
from app.services import CatalogosService
from dependency_injector import containers
from dependency_injector.wiring import inject, Provide
from models.motocicletas import Motocicleta

router = APIRouter()


@router.get("/motocicletas")
@inject
async def get_all_motocicletas(
    limit: str = 10,
    offset: str = 0,
    marca: str | None = Query(None, description="Filtrar por marca de motocicleta"),
    catalogo_repo=Depends(Provide[Container.repositorio_catalogos]),
):
    service = CatalogosService(catalogo_repo=catalogo_repo)
    result = await service.obtener_motocicletas()
    
    return {"response": result}


@router.get("/sucursales")
async def get_all_sucursales():
    return {"response": "ok"}
