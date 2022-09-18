from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from config.db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uid = Column(String(255))
    fullname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    keyConfirm = Column(String(255))
    isConfirmed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)
