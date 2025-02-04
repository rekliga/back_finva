from domain.category_repository import CatalogoRepository
from models.motocicletas import Motocicleta


class CatalogosService:
    def __init__(self, catalogo_repo: CatalogoRepository):
        self.catalogo_repo = catalogo_repo

    async def obtener_motocicletas(
        self, modelo: str = "", limit: str = 10, offset: str = 0
    ):
        motocicletas = await self.catalogo_repo.get_motocicletas(limit, offset, modelo)
        resultado = [
        Motocicleta(id=moto[0], marca=moto[1], modelo=moto[2], año=moto[3])
        for moto in motocicletas
    ]
        return resultado
