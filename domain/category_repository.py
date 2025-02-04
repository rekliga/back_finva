from abc import ABC, abstractmethod


class CatalogoRepository(ABC):
    @abstractmethod
    async def get_motocicletas(limit: int = 10, offset: int = 0):
        pass

    @abstractmethod
    async def get_sucursales(limit: int = 10, offset: int = 0):
        pass

    