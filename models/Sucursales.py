from pydantic import BaseModel


class Sucursal(BaseModel):
    id: int
    nombre: str
    calle: str
    numero_exterior: int
    ciudad: str
    estado: str
    lat:float
    lng:float
