# app/routers/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.users import UserCreate, User
from app.crud.users import create_user, authenticate_user, create_access_token_for_user
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=User)
async def register(user: UserCreate):
    existing_user = await authenticate_user(user.username, user.password)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return await create_user(user)

@router.post("/token")
async def login_for_access_token(form_data: UserCreate):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}

