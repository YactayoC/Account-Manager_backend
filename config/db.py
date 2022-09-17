from sqlalchemy import create_engine, MetaData
import pymysql
from os import getenv

engine = create_engine("mysql+pymysql://root:sebas2001@localhost:3306/account_manager")
meta = MetaData()
conn = engine.connect()

