from abc import ABC, abstractmethod

from models.Formularios import FormularioRegistro


class UsersRepository(ABC):
    @abstractmethod
    async def create_user(request:FormularioRegistro):
        pass
