import uuid

from config.db import conn
from models.account import accounts
from schemas.account import Account


def insertAccount(account: dict):
    account["aid"] = uuid.uuid4()
    conn.execute(accounts.insert().values(account))


def getAccount(aid: str):
    accountDB = conn.execute(accounts.select().where(accounts.c.aid == aid)).first()
    return accountDB


def getAccounts(uid: str):
    accountsDB = conn.execute(accounts.select().where(accounts.c.uid == uid)).fetchall()
    return accountsDB


def updateAccount(data: dict, aid: str):
    conn.execute(accounts.update().values(data).where(accounts.c.aid == aid))


def deleteAccount(aid: str):
    conn.execute(accounts.delete().where(accounts.c.aid == aid))
