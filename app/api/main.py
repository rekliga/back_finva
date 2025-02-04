from fastapi import FastAPI
from app.api.endpoints.api_routes import api_router
from infraestructure.dependencias.containers import Container


app = FastAPI()
app.include_router(api_router)
container = Container()
container.init_resources()
container.wire(modules=["app.api.endpoints.catalogos","app.api.endpoints.formularios"])


@app.on_event("shutdown")
async def shutdown():
    container.shutdown_resources()
