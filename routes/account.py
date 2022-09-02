from fastapi import APIRouter, Header
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from config.db import conn
from models.account import accounts
from schemas.account import Account
from middlewares.verify_token import VerifyTokenRoute

account_routes = APIRouter(route_class=VerifyTokenRoute)


@account_routes.post("/add-account")
async def add_account(req: Request):
    try:
        new_user = await req.json()
        new_user["password"] = hashpw(new_user["password"].encode("utf-8"), gensalt(10))
        result = conn.execute(users.insert().values(new_user))
        return JSONResponse({"ok": True, "msg": "User registered successfully"}, 201)
    except Exception:
        return JSONResponse(
            {"ok": False, "msg": "The email address is registered"}, 400
        )


@account_routes.post("/get-account/{aid}")
async def update_account(req: Request):
    return "get__account"


@account_routes.post("/update-account/{aid}")
async def update_account(req: Request):
    return "update__acount"


@account_routes.post("/delete-account/{aid}")
async def delete_account(req: Request):
    return "delete__acount"
