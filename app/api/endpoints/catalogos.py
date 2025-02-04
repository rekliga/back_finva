from fastapi import APIRouter, Depends, HTTPException, Query
from infraestructure.dependencias.containers import Container
from app.services import CatalogosService
from dependency_injector.wiring import inject, Provide
from models.responses import SuccessResponse, ErrorResponse
from fastapi.security import HTTPBearer
from app.utils.utils import BearerToken, decode_token

router = APIRouter()
oauth2_scheme = HTTPBearer()


@router.get("/motocicletas", response_model=SuccessResponse)
@inject
async def get_all_motocicletas(
    limit: int = 10,
    offset: int = 0,
    marca: str | None = Query(None, description="Filtrar por marca de motocicleta"),
    catalogo_repo=Depends(Provide[Container.repositorio_catalogos]),
    token: HTTPBearer = Depends(oauth2_scheme),
):
    try:
        token_data: BearerToken = await decode_token(token.credentials)
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
@inject
async def get_all_sucursales(
    limit: int = 10,
    offset: int = 0,
    catalogo_repo=Depends(Provide[Container.repositorio_catalogos]),
    token: HTTPBearer = Depends(oauth2_scheme),
):
    try:
        token_data: BearerToken = await decode_token(token.credentials)
        service = CatalogosService(catalogo_repo=catalogo_repo)
        result = await service.obtener_sucursales(
            limit=limit,
            offset=offset,
        )
    except Exception as e:
        return ErrorResponse(message=str(e), status_code=500)
    return SuccessResponse(
        message="El recurso se consuto con exito", data={"result": result}
    )


@router.get("/sucursales/nearest")
@inject
async def closes_sucursal(
    longitud: float,
    latitude: float,
    catalogo_repo=Depends(Provide[Container.repositorio_catalogos]),
    token: HTTPBearer = Depends(oauth2_scheme),
):
    try:
        token_data: BearerToken = await decode_token(token.credentials)
        service = CatalogosService(catalogo_repo=catalogo_repo)
        result = await service.obtener_sucursal_cercana(
            longitud=longitud, latitute=latitude
        )
    except Exception as e:
        return ErrorResponse(message=str(e), status_code=500)
    return SuccessResponse(
        message="Sucursal más cercana encontrada", data={"result": result}
    )
