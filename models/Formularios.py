from pydantic import BaseModel


class FormularioRegistro(BaseModel):
    nombre: str
    segundo_nombre: str
    apellido: str
    segundo_apellido: str
    email: str
    id_motocicleta: int
    calle: str
    numero_interior: int
    numero_exterior: int
    ciudad: str
    estado: str
