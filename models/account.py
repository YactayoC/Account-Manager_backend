from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
import uuid

from config.db import meta, engine

accounts = Table(
    "accounts",
    meta,
    Column("id", Integer, primary_key=True),
    Column("aid", String(255), default=uuid.uuid4()),
    Column("uid", String(255)),
    Column("category", String(255), nullable=False),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
)

meta.create_all(engine)
