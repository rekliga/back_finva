from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBearer
from app.services import UserService
from app.utils.utils import BearerToken, decode_token
from infraestructure.dependencias.containers import Container
from dependency_injector.wiring import inject, Provide
from models.Formularios import FormularioRegistro
from models.responses import SuccessResponse, ErrorResponse

router = APIRouter()
oauth2_scheme = HTTPBearer()


@router.post("/register", response_model=SuccessResponse)
@inject
async def register_new_user(
    request: FormularioRegistro,
    user_repository=Depends(Provide[Container.repositorio_users]),
    token: HTTPBearer = Depends(oauth2_scheme),
):
    try:
        token_data: BearerToken = await decode_token(token.credentials)

        service = UserService(user_repository=user_repository)
        await service.registro_cliente(request)
    except Exception as e:
        return ErrorResponse(message=str(e))
    return SuccessResponse(message="Registro Enviado", data=request.model_dump())
