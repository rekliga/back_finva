from sqlalchemy import Table, Column, Integer, String, Float
from infraestructure.db import metadata

sucursales = Table(
    "sucursales",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(50), nullable=False),
    Column("calle", String(50), nullable=False),
    Column("numero exterior", Integer, nullable=False),
    Column("ciudad", String(50), nullable=False),
    Column("estado", String(50), nullable=False),
    Column("lat", Float, nullable=True),
    Column("lng", Float, nullable=True),
)
