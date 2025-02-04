from sqlalchemy import ForeignKey, Table, Column, Integer, String
from infraestructure.db import metadata

usuarios = Table(
    "usuarios",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(50), nullable=False),
    Column("segundo_nombre", String(50), nullable=True),
    Column("apellido", String(50), nullable=False),
    Column("segundo_apellido", String(50), nullable=True),
    Column("email", String(100), nullable=False, unique=True),
    Column("id_motocicleta", Integer, ForeignKey("motocicletas.id"), nullable=False),
    Column("calle", String(100), nullable=True),
    Column("numero_interior", Integer, nullable=True),
    Column("numero_exterior", Integer, nullable=True),
    Column("ciudad", String(50), nullable=True),
    Column("estado", String(50), nullable=True)
)