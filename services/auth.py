from sqlalchemy.orm import Session
from bcrypt import hashpw, checkpw, gensalt
import uuid
import time

from config.db import SessionLocal
from models.user import User as UserModel
from schemas.user import User as UserSchema
from utils.to_dict import object_as_dict

db: Session = SessionLocal()


def insertUser(user: dict):
    user["uid"] = uuid.uuid4();
    user["keyConfirm"] = int(round(time.time() * 1000))
    user["password"] = hashpw(user["password"].encode("utf-8"), gensalt(10))
    new_user = UserModel(uid=user["uid"], fullname=user["fullname"], email=user["email"], password=user["password"], keyConfirm=user["keyConfirm"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def getUser(uid: str):
    userDB = db.query(UserModel).filter_by(uid=uid).first()
    userDB = object_as_dict(userDB)
    return userDB


def getUserByEmail(email: str, returnDict: bool = False):
    userDB =  db.query(UserModel).filter_by(email=email).first()

    if (returnDict):
        userDB = object_as_dict(userDB)
    return userDB

def getUserUpdateConfirm(uid: str):
    db.query(UserModel).filter_by(uid=uid).update({"keyConfirm": None, "isConfirmed": True})
    db.commit()
