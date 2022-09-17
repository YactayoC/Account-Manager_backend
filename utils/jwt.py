from os import getenv
from datetime import datetime, timedelta
from token import *

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt


class AuthHandler:
    bearer = HTTPBearer()

    def encode_token(self, uid: str):
        payload = {
            "uid": uid,
            "exp": datetime.utcnow() + timedelta(days=1),
        }

        token = jwt.encode(payload, getenv("JWT_SECRET_KEY"), algorithm="HS256")
        return token

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
            return payload["uid"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(bearer)):
        return self.decode_token(auth.credentials)
