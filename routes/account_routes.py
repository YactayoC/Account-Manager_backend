from fastapi import APIRouter, Header
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from config.db import conn
from models.account import accounts
from schemas.account import Account
from middlewares.verify_token import VerifyTokenRoute

account_routes = APIRouter(route_class=VerifyTokenRoute)

# Hacer que el middleware guarde el uid del usuario
@account_routes.post("/add-account")
async def add_account(req: Request):
    try:
        new_account = await req.json()
        result = conn.execute(accounts.insert().values(new_account))
        return JSONResponse({"ok": True, "msg": "Account added successfully"}, 201)
    except Exception:
        return JSONResponse({"ok": False, "msg": error}, 400)


@account_routes.get("/get-accounts")
def get_accounts(req: Request):
    print(req.headers)
    # accountsDB = conn.execute(accounts.select()).fetchall()
    return {"accounts"}


@account_routes.get("/get-account/{aid}")
def update_account(req: Request, aid: str):
    try:
        account_DB = conn.execute(
            accounts.select().where(accounts.c.aid == aid)
        ).first()

        if not account_DB:
            return JSONResponse(
                {"ok": False, "msg": "There is no account with this aid"}, 400
            )

        return {"ok": True, "account": account_DB}
    except Exception as error:
        return JSONResponse({"ok": False, "msg": error}, 400)


@account_routes.post("/update-account/{aid}")
def update_account(aid: str, account: Account):
    data = {
        "email": account.email,
        "category": account.category,
        "password": account.password,
    }

    try:
        accountDB = conn.execute(accounts.select().where(accounts.c.aid == aid)).first()

        if not (accountDB):
            return JSONResponse(
                {"ok": False, "msg": "There is no account with this aid"}, 400
            )

        accountDB_Update = conn.execute(
            accounts.update().values(data).where(accounts.c.aid == aid)
        )
        return JSONResponse({"msg": "Account updated successfully"}, 202)

    except Exception as error:
        print(error)
        return {"msg": error}


@account_routes.post("/delete-account/{aid}")
async def delete_account(req: Request):
    return "delete__acount"
