from fastapi import FastAPI
from app.api.endpoints.api_routes import api_router
from infraestructure.dependencias.containers import Container


app = FastAPI()
app.include_router(api_router)
container = Container()
container.init_resources()  # Inicializa recursos necesarios
container.wire(
    modules=["app.api.endpoints.catalogos"]
)
