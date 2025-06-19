from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        token = auth.credentials

        try:
            data = validate_token(token)
            # Comprobamos que tenga email y sea admin
            if data.get("email") != "admin@gmail.com":
                raise HTTPException(status_code=403, detail="Acceso no autorizado")
        except Exception as e:
            raise HTTPException(status_code=403, detail=str(e))
