from dependency_injector import containers, providers
from infraestructure.db import get_session
from infraestructure.repositories.catalogo_repository import CatalogoSQLRepository
from sqlalchemy.ext.asyncio import AsyncSession


class Container(containers.DeclarativeContainer):
    session_factory = providers.Factory(get_session)
    repositorio_catalogos = providers.Factory(
        CatalogoSQLRepository,
        session=session_factory,
    )
