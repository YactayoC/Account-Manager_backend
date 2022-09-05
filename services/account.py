from config.db import conn
from models.account import accounts
from schemas.account import Account


async def insertAccount(account: dict):
    conn.execute(accounts.insert().values(account))


async def getAccount(aid: str):
    accountDB = conn.execute(accounts.select().where(accounts.c.aid == aid)).first()
    return accountDB


async def getAccounts(uid: str):
    accountsDB = conn.execute(accounts.select().where(accounts.c.uid == uid)).fetchall()
    return accountsDB


async def updateAccount(data: dict, aid: str):
    conn.execute(accounts.update().values(data).where(accounts.c.aid == aid))


async def deleteAccount(aid: str):
    conn.execute(accounts.delete().where(accounts.c.aid == aid))
