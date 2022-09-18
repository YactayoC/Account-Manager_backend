from sqlalchemy import Column, Integer, String, UniqueConstraint
from config.db import Base, engine


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    aid = Column(String(255))
    uid = Column(String(255))
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    category = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    UniqueConstraint("aid")


Base.metadata.create_all(bind=engine)
