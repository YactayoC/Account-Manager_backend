from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_NAME = config("DB_NAME")
DB_SSL = config("DB_SSL")

MYSQL_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
CONFIG_SSL = {
    "ssl": {
        "ssl_ca": DB_SSL,
    }
}

engine = create_engine(MYSQL_URI, connect_args=CONFIG_SSL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
