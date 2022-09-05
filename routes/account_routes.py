from fastapi import APIRouter, Header, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from services.account import *
from utils.jwt import AuthHandler

account_routes = APIRouter()
auth_handler = AuthHandler()


@account_routes.post("/add-account")
async def add_account(req: Request, uid=Depends(auth_handler.auth_wrapper)):
    try:
        new_account = await req.json()
        new_account["uid"] = uid
        result = await insertAccount(new_account)
        return JSONResponse({"ok": True, "msg": "Account added successfully"}, 201)
    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


@account_routes.get("/get-accounts")
async def get_accounts(uid=Depends(auth_handler.auth_wrapper)):
    accountsDB = await getAccounts(uid)
    return {"ok": True, "accounts": accountsDB}


@account_routes.get("/get-account/{aid}")
async def update_account(aid: str, uid=Depends(auth_handler.auth_wrapper)):
    try:
        account_DB = await getAccount(aid)

        if not account_DB:
            return JSONResponse(
                {"ok": False, "msg": "There is no account with this aid"}, 400
            )

        return {"ok": True, "account": account_DB}
    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


@account_routes.post("/update-account/{aid}")
async def update_account(
    req: Request, aid: str, uid=Depends(auth_handler.auth_wrapper)
):

    data = await req.json()

    try:
        accountDB = await getAccount(aid)

        if not (accountDB):
            return JSONResponse(
                {"ok": False, "msg": "There is no account with this aid"}, 400
            )

        accountDB_Update = await updateAccount(data, aid)
        return JSONResponse({"ok": True, "msg": "Account updated successfully"}, 202)

    except Exception as error:
        return {"ok": False, "msg": "There was an error"}


@account_routes.post("/delete-account/{aid}")
async def delete_account(aid: str):
    # Todo: validar si aun existe
    await deleteAccount(aid)
    return JSONResponse({"ok": True, "msg": "Account updated successfully"}, 202)
