from sqlalchemy.ext.asyncio import AsyncSession
from domain.category_repository import CatalogoRepository
from infraestructure.tables.motocicletas import motocicletas
from sqlalchemy import select


class CatalogoSQLRepository(CatalogoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_motocicletas(self, limit: int, offset: int, marca: str = None):
        session_instance = await anext(self.session)
        if marca:
            query = select(motocicletas).where(motocicletas.c.marca == marca)
        else:
            query = select(motocicletas)

        query = query.offset(offset).limit(limit)

        result = await session_instance.execute(query)
        return result.all()
    async def get_sucursales(self,limit:int,offset:int):
        ...