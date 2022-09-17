from bcrypt import hashpw, checkpw, gensalt
import uuid
import time

from config.db import conn
from models.user import users
from schemas.user import User


def insertUser(user: dict):
    user["uid"] = uuid.uuid4();
    user["keyConfirm"] = int(round(time.time() * 1000))
    user["password"] = hashpw(user["password"].encode("utf-8"), gensalt(10))
    conn.execute(users.insert().values(user))


def getUser(uid: str):
    userDB = conn.execute(users.select().where(users.c.uid == uid)).first()
    return userDB


def getUserByEmail(email: str):
    userDB = conn.execute(users.select().where(users.c.email == email)).first()
    return userDB
