from fastapi import APIRouter, Header
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from bcrypt import hashpw, checkpw, gensalt

from utils.jwt import write_token, validate_token
from services.auth import insertUser, getUserByEmail
from utils.validations_user import areValidFields, isEmailValid

auth_routes = APIRouter()


@auth_routes.post("/register")
async def register_user(req: Request):
    new_user = await req.json()

    try:
        if areValidFields(new_user):
            return JSONResponse({"ok": False, "msg": "Invalid Fields"}, 400)

        userDB = await getUserByEmail(new_user["email"])

        if userDB:
            return JSONResponse({"ok": False, "msg": "User already registered"}, 400)

        await insertUser(new_user)
        return JSONResponse({"ok": True, "msg": "User registered successfully"}, 201)
    except:
        return JSONResponse({"ok": False, "msg": "There was an error registering"}, 400)


@auth_routes.post("/login")
async def login_user(req: Request):
    user = await req.json()

    try:
        emailvalid = isEmailValid(user["email"])

        if not isEmailValid(user["email"]):
            return JSONResponse({"ok": False, "msg": "Email is not valid"}, 400)

        userDB = await getUserByEmail(user["email"])

        if not userDB:
            return JSONResponse({"ok": False, "msg": "User not found"}, 400)

        if not checkpw(
            user["password"].encode("utf-8"), userDB.password.encode("utf-8")
        ):
            return JSONResponse(
                {"ok": False, "msg": "Incorrect email or password"}, 400
            )

        token = write_token(userDB)
        return JSONResponse({"ok": True, "token": token}, 200)
    except Exception as error:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


@auth_routes.post("/revalidate-token")
def revalidate_token(Authorization: str = Header()):
    token = Authorization.split(" ")[1]
    uid = validate_token(token, True)["uid"]

    if token:
        return JSONResponse({"ok": True, "uid": uid}, 400)


# Confirmar cuenta
@auth_routes.post("/confirm-user/{keyConfirm}")
def confirm_user():
    return "Hello worlds"
