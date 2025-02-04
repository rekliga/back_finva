from abc import ABC, abstractmethod


class CatalogoRepository(ABC):
    @abstractmethod
    async def get_motocicletas():
        pass

    @abstractmethod
    async def get_sucursales():
        pass
