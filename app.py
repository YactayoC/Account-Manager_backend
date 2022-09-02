from fastapi import FastAPI
from dotenv import load_dotenv

from routes.auth import auth_routes
from routes.account import account_routes

load_dotenv()
app = FastAPI()

app.include_router(auth_routes, prefix="/api/auth")
app.include_router(account_routes, prefix="/api/account")
