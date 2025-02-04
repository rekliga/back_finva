from sqlalchemy.ext.asyncio import AsyncSession
from domain.category_repository import CatalogoRepository
from infraestructure.tables.motocicletas import motocicletas
from infraestructure.tables.sucursales import sucursales
from sqlalchemy import select

from models.Sucursales import Sucursal


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

    async def get_sucursales(self, limit: int = 10, offset: int = 0):
        session_instance = await anext(self.session)
        query = select(sucursales).offset(offset).limit(limit)
        result = await session_instance.execute(query)
        agencias = result.all()
        resultado = [
            Sucursal(
                id=sucursal[0],
                nombre=sucursal[1],
                calle=sucursal[2],
                numero_exterior=sucursal[3],
                ciudad=sucursal[4],
                estado=sucursal[5],
                lat=sucursal[6],
                lng=sucursal[7]
            )
            for sucursal in agencias
        ]
        return resultado
