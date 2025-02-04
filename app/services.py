from domain.category_repository import CatalogoRepository
from infraestructure.external_services.google_maps_service import GoogleMapsService
from models.Sucursales import Sucursal
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
        sucursales = await self.catalogo_repo.get_sucursales(limit, offset)
        return sucursales

    async def obtener_sucursal_cercana(self, latitute: float, longitud: float):
        sucursales = await self.catalogo_repo.get_sucursales()
        result = await GoogleMapsService.get_nearest_sucursal(latitute, longitud,sucursales)
        return result
