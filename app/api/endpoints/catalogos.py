from fastapi import APIRouter, Depends, HTTPException, Query
from infraestructure.dependencias.containers import Container
from app.services import CatalogosService
from dependency_injector import containers
from dependency_injector.wiring import inject, Provide
from models.motocicletas import Motocicleta
from models.responses import SuccessResponse, ErrorResponse

router = APIRouter()


@router.get("/motocicletas", response_model=SuccessResponse)
@inject
async def get_all_motocicletas(
    limit: int = 10,
    offset: int = 0,
    marca: str | None = Query(None, description="Filtrar por marca de motocicleta"),
    catalogo_repo=Depends(Provide[Container.repositorio_catalogos]),
):
    try:
        service = CatalogosService(catalogo_repo=catalogo_repo)
        result = await service.obtener_motocicletas(
            limit=limit, offset=offset, marca=marca
        )
    except Exception as e:
        return ErrorResponse(message=str(e), status_code=500)
    return SuccessResponse(
        message="El recurso se consuto con exito", data={"result": result}
    )


@router.get("/sucursales")
async def get_all_sucursales(
    limit: int = 10,
    offset: int = 0,
):
    try:
        ...
    except Exception as e:
        return ErrorResponse(message=str(e))
    return SuccessResponse(
        message="El recurso se consuto con exito", data={"result": result}
    )
