from sqlalchemy import Table, Column, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

accounts = Table(
    "accounts",
    meta,
    Column("id", Integer, primary_key=True),
    Column("aid", String(255)),
    Column("uid", String(255)),
    Column("title", String(255), nullable=False),
    Column("description", String(255)),
    Column("category", String(255), nullable=False),
    Column("email", String(255), nullable=False),
    Column("password", String(255), nullable=False),
    UniqueConstraint("aid"),
)


meta.create_all(engine)
