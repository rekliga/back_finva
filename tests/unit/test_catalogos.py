import pytest
from httpx import AsyncClient
from fastapi import status
from app.api.main import app
from infraestructure.dependencias.containers import Container
from app.utils.utils import BearerToken


class DummyCatalogoRepository:
    async def obtener_motocicletas(self, limit: int, offset: int, marca: str = None):

        return [{"id": 1, "marca": marca or "Dummy", "modelo": "Model X", "anio": 2021}]

    async def obtener_sucursales(self, limit: int, offset: int):

        return [
            {
                "id": 1,
                "nombre": "Sucursal Dummy",
                "calle": "Calle Dummy",
                "numero_exterior": 100,
                "ciudad": "Ciudad Dummy",
                "estado": "Estado Dummy",
            }
        ]

    async def obtener_sucursal_cercana(self, longitud: float, latitute: float):

        return {"id": 1, "nombre": "Sucursal Dummy", "distancia": 0.5}


app.dependency_overrides[Container.repositorio_catalogos] = (
    lambda: DummyCatalogoRepository()
)


async def dummy_decode_token(token: str) -> BearerToken:

    return BearerToken(user_id=1, token=token)


from app.utils import utils

app.dependency_overrides[utils.decode_token] = dummy_decode_token


@pytest.mark.asyncio
async def test_get_all_motocicletas():
    async with AsyncClient(app=app, base_url="http://test") as client:
        headers = {"Authorization": "Bearer dummy-token"}
        response = await client.get(
            "/motocicletas",
            params={"limit": 5, "offset": 0, "marca": "KTM"},
            headers=headers,
        )

        assert response.status_code == status.HTTP_200_OK
        json_data = response.json()

        assert "message" in json_data
        assert "data" in json_data
        assert "result" in json_data["data"]

        assert isinstance(json_data["data"]["result"], list)
        assert len(json_data["data"]["result"]) > 0


@pytest.mark.asyncio
async def test_get_all_sucursales():
    async with AsyncClient(app=app, base_url="http://test") as client:
        headers = {"Authorization": "Bearer dummy-token"}
        response = await client.get(
            "/sucursales",
            params={"limit": 5, "offset": 0},
            headers=headers,
        )
        assert response.status_code == status.HTTP_200_OK
        json_data = response.json()
        assert "message" in json_data
        assert "data" in json_data
        assert "result" in json_data["data"]
        assert isinstance(json_data["data"]["result"], list)
        assert len(json_data["data"]["result"]) > 0


@pytest.mark.asyncio
async def test_get_nearest_sucursal():
    async with AsyncClient(app=app, base_url="http://test") as client:
        headers = {"Authorization": "Bearer dummy-token"}

        response = await client.get(
            "/sucursales/nearest",
            params={"longitud": -99.1332, "latitude": 19.4326},
            headers=headers,
        )
        assert response.status_code == status.HTTP_200_OK
        json_data = response.json()
        assert "message" in json_data
        assert "data" in json_data
        assert "result" in json_data["data"]

        assert isinstance(json_data["data"]["result"], dict)
