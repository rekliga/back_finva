from pydantic import BaseModel


class Motocicleta(BaseModel):
    id: int
    marca: str
    modelo: str
    año: int
