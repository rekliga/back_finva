from sqlalchemy import Table, Column, Integer, String
from infraestructure.db import metadata

motocicletas = Table(
    "motocicletas",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("marca", String(50), nullable=False),
    Column("modelo", String(50), nullable=False),
    Column("anio", Integer, nullable=True),
)
