import uuid
from sqlalchemy.orm import Session

from config.db import SessionLocal
from models.account import Account as AccountModel
from schemas.account import Account as AccountSchema
from utils.to_dict import object_as_dict

db: Session = SessionLocal()

def insertAccount(account: dict):
    account["aid"] = uuid.uuid4()
    new_account = AccountModel(aid = account["aid"], uid= account["uid"], title = account["title"], description = account["description"], category = account["category"], email = account["email"], password = account["password"])
    db.add(new_account)
    db.commit()
    db.refresh(new_account)


def getAccount(aid: str):
    accountDB = db.query(AccountModel).filter_by(aid=aid).first()
    accountDB = object_as_dict(accountDB)
    return accountDB


def getAccounts(uid: str):
    accountsDB = db.query(AccountModel).filter_by(uid=uid).all()
    return accountsDB


def updateAccount(data: dict, aid: str):
    db.query(AccountModel).filter_by(aid=aid).update(data)
    db.commit()


def deleteAccount(aid: str):
    accountDB = db.query(AccountModel).filter_by(aid=aid).first()
    db.delete(accountDB)
    db.commit()

def searchAccount(value: str):
    accountsDB = db.query(AccountModel).filter(AccountModel.title.like('%' + value + '%')).all()
    return accountsDB
