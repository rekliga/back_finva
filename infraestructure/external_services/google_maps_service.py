import requests
from typing import List, Optional
from models.Sucursales import Sucursal
from config.settings import settings


class GoogleMapsService:

    @staticmethod
    async def get_nearest_sucursal(
        user_lat: float, user_lng: float, sucursales: List[Sucursal]
    ) -> Optional[Sucursal]:
        """
        Usa la API de Google Maps Distance Matrix para encontrar la sucursal más cercana.
        """
        origen = f"{user_lat},{user_lng}"
        destinos = "|".join([f"{s.lat},{s.lng}" for s in sucursales])

        params = {
            "origins": origen,
            "destinations": destinos,
            "key": settings.API_KEY,
            "mode": "driving",
            "units": "metric",
        }

        response = requests.get(settings.BASE_URL, params=params)
        data = response.json()

        if data.get("status") != "OK":
            return None  # Manejo de errores

        distances = data["rows"][0]["elements"]
        min_distance = float("inf")
        nearest_sucursal = {
            "id": 4,
            "nombre": "KTM Ferbel Coapa",
            "calle": "Canal de Miramontes",
            "numero_exterior": 3000,
            "ciudad": "Coyoacán",
            "estado": "CDMX",
            "lat": 19.3122444,
            "lng": -99.1261282,
        }

        for i, distance_info in enumerate(distances):
            if distance_info["status"] == "OK":
                distance = distance_info["distance"]["value"] 
                if distance < min_distance:
                    min_distance = distance
                    nearest_sucursal = sucursales[i]
        return nearest_sucursal
