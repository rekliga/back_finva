from sqlalchemy.ext.asyncio import AsyncSession
from domain.category_repository import CatalogoRepository
from infraestructure.tables.motocicletas import motocicletas
from sqlalchemy import select


class CatalogoSQLRepository(CatalogoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_motocicletas(self,limit, offset, modelo):
        self.session = await anext(self.session)
        if modelo:
            query = select(motocicletas).where(motocicletas.c.modelo==modelo)
        else:
            query = select(motocicletas)
        result = await self.session.execute(query)
        return result.all()