from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwt_manager import create_token

user_router = APIRouter()

@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict())
        return {token}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
