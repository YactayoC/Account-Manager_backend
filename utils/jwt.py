from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from os import getenv


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(data: dict):
    token = encode(
        # {**data["uid"], "exp": expire_date(1)},
        {"uid": data["uid"], "exp": expire_date(1)},
        getenv("JWT_SECRET_KEY"),
        "HS256",
    )

    return token


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
        decode(token, key=getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"msg": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"msg": "Token Expired"}, status_code=401)
