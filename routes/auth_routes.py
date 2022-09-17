from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from bcrypt import checkpw

from utils.jwt import AuthHandler
from utils.validations_user import areValidFields, isEmailValid
from services.auth import insertUser, getUserByEmail, getUser

auth_routes = APIRouter()
auth_handler = AuthHandler()


@auth_routes.post("/register")
async def register_user(req: Request):
    new_user = await req.json()

    try:
        if areValidFields(new_user):
            return JSONResponse({"ok": False, "msg": "Invalid Fields"}, 400)

        userDB = getUserByEmail(new_user["email"])

        if userDB:
            return JSONResponse({"ok": False, "msg": "User already registered"}, 400)

        insertUser(new_user)
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

        userDB = getUserByEmail(user["email"])

        if not userDB:
            return JSONResponse({"ok": False, "msg": "User not found"}, 400)

        if not checkpw(user["password"].encode("utf-8"), userDB.password.encode("utf-8")):
            return JSONResponse({"ok": False, "msg": "Incorrect email or password"}, 400)

        token = auth_handler.encode_token(userDB.uid)
        return JSONResponse({"ok": True, "user": dict(userDB), "token": token}, 200)
    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


@auth_routes.get("/revalidate-token")
def revalidate_token(uid=Depends(auth_handler.auth_wrapper)):

    try:
        if not (uid):
            return JSONResponse({"ok": False, "msg": "Invalid token"}, 401)

        userDB = getUser(uid)

        if not (userDB):
            return JSONResponse({"ok": False, "msg": "Not found user"}, 404)

        token = auth_handler.encode_token(userDB.uid)
        return JSONResponse({"ok": True, "user": dict(userDB), "token": token}, 200)
    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


# todo: Confirmar cuenta
@auth_routes.post("/confirm-user/{keyConfirm}")
def confirm_user():
    return "Hello worlds"
