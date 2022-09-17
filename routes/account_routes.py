from fastapi import APIRouter, Depends
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
        new_account["category"] = new_account["category"].lower().strip()
        new_account["uid"] = uid
        result = insertAccount(new_account)
        return JSONResponse({"ok": True, "msg": "Account added successfully"}, 201)
    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)



#todo: Posible error
@account_routes.get("/get-accounts")
def get_accounts(uid=Depends(auth_handler.auth_wrapper)):
    accountsDB = getAccounts(uid)
    return {"ok": True, "accounts": accountsDB}


# @account_routes.get("/get-account/{aid}")
# async def update_account(aid: str, uid=Depends(auth_handler.auth_wrapper)):
#     try:
#         account_DB = await getAccount(aid)

#         if not account_DB:
#             return {"ok": False, "msg": "There is no account with this aid"}

#         return {"ok": True, "account": account_DB}
#     except:
#         return {"ok": False, "msg": "There was an error"}


@account_routes.put("/update-account/{aid}")
async def update_account(req: Request, aid: str, uid=Depends(auth_handler.auth_wrapper)):

    data = await req.json()

    try:
        accountDB = getAccount(aid)

        if not (accountDB):
            return JSONResponse({"ok": False, "msg": "There is no account with this aid"}, 400)

        accountDB_update = updateAccount(data, aid)
        return JSONResponse({"ok": True, "msg": "Account updated successfully"}, 202)

    except:
        return JSONResponse({"ok": False, "msg": "There was an error"}, 400)


@account_routes.delete("/delete-account/{aid}")
async def delete_account(aid: str):
    deleteAccount(aid)
    return JSONResponse({"ok": True, "msg": "Account updated successfully"}, 202)


@account_routes.get("/search-account/{aid}")
async def search_account(aid: str):
    deleteAccount(aid)
    return JSONResponse({"ok": True, "msg": "Account updated successfully"}, 202)
