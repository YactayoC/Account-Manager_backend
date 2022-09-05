from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt2 import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, details="Invalidate or Expired Token"
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details="Invalidate or Expired Token")

    def verify_jwt(self, token: str):
        isTokenValid: bool = False
        payload = decodeJWT(token)
        if payload:
            isTokenValid = True
        return isTokenValid
