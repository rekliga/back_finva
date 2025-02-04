from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import MetaData
from dependency_injector.wiring import Provide, inject
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import settings
# Define la URL de conexión (ajusta usuario, contraseña, host, puerto y base de datos)
if settings.enviroment != "local":
    DATABASE_URL = f"postgresql+asyncpg://{settings.user}:{settings.password}@{settings.host}/{settings.bd_name}"
else:
    DATABASE_URL = f"postgresql+asyncpg://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.bd_name}"


engine = create_async_engine(DATABASE_URL, echo=False)

metadata = MetaData()

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
