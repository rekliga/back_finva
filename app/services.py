from domain.category_repository import CatalogoRepository
from models.motocicletas import Motocicleta


class CatalogosService:
    def __init__(self, catalogo_repo: CatalogoRepository):
        self.catalogo_repo = catalogo_repo

    async def obtener_motocicletas(
        self, marca: str = "", limit: int = 10, offset: int = 0
    ):
        motocicletas = await self.catalogo_repo.get_motocicletas(limit, offset, marca)
        resultado = [
            Motocicleta(id=moto[0], marca=moto[1], modelo=moto[2], año=moto[3])
            for moto in motocicletas
        ]
        return resultado

    async def obtener_sucursales(self, limit: int = 10, offset: int = 0): 
        sucursales = await self.catalogo_repo.get_sucursales(limit,offset)