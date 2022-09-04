from bcrypt import hashpw, checkpw, gensalt

from config.db import conn
from models.user import users
from schemas.user import User


async def insertUser(user: dict):
    user["password"] = hashpw(user["password"].encode("utf-8"), gensalt(10))
    await conn.execute(users.insert().values(user))


async def getUserByEmail(email: str):
    userDB = conn.execute(users.select().where(users.c.email == email)).first()
    return userDB
