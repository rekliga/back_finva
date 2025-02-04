from sqlalchemy.ext.asyncio import AsyncSession
from domain.user_repository import UsersRepository
from models.Formularios import FormularioRegistro
from sqlalchemy import insert
from infraestructure.tables.users import usuarios


class UsersSQLRepository(UsersRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    async def create_user(self,request:FormularioRegistro):
        session_instance = await anext(self.session)
        query = insert(usuarios).values(request.model_dump())
        await session_instance.execute(query)
        await session_instance.commit()
