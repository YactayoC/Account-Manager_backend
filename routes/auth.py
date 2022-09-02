from fastapi import APIRouter, Header
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from bcrypt import hashpw, checkpw, gensalt

from config.db import conn
from models.user import users
from schemas.user import User
from utils.jwt import write_token, validate_token

auth_routes = APIRouter()


@auth_routes.post("/register")
async def register_user(req: Request):
    try:
        new_user = await req.json()
        new_user["password"] = hashpw(new_user["password"].encode("utf-8"), gensalt(10))
        result = conn.execute(users.insert().values(new_user))
        return JSONResponse({"ok": True, "msg": "User registered successfully"}, 201)
    except Exception:
        return JSONResponse(
            {"ok": False, "msg": "The email address is registered"}, 400
        )


@auth_routes.post("/login")
async def login_user(req: Request):
    user = await req.json()

    try:
        userDB = conn.execute(
            users.select().where(users.c.email == user["email"])
        ).first()

        if not userDB:
            return JSONResponse({"hassError": False, "msg": "User not found"}, 400)

        if not checkpw(
            user["password"].encode("utf-8"), userDB.password.encode("utf-8")
        ):
            return JSONResponse(
                {"hassError": False, "msg": "Email or password incorrect"}, 400
            )

        token = write_token(userDB)

        return JSONResponse({"ok": True, "user": userDB, "token": token}, 200)
    except Exception:
        return JSONResponse(
            {"ok": False, "msg": "Some fields is empty or invalid"}, 400
        )


@auth_routes.post("/revalidate-token")
def revalidate_token(Authorization: str = Header()):
    token = Authorization.split(" ")[1]

    if token:
        return JSONResponse({"ok": True, "token": validate_token(token)}, 400)


# Confirmar cuenta
@auth_routes.post("/confirm-user/{keyConfirm}")
def confirm_user():
    return "Hello worlds"
