from typing import Annotated
from datetime import datetime

from fastapi import Path, HTTPException, Query, APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.users import UserModel
from app.schemas.users import UserCreateRequest, UserUpdateRequest, UserSearchParams, Token
from app.utils.jwt import create_access_token, get_current_user

user_router = APIRouter(prefix="/users", tags=["user"])

@user_router.post("")
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id

@user_router.get("")
async def get_all_users():
    users = UserModel.all()
    if not users:
        raise HTTPException(status_code=404)
    return users

@user_router.get("/search")
async def search_users(query_params: Annotated[UserSearchParams, Query()]):
    valid_query = {k: v for k, v in query_params.model_dump().items() if v is not None}
    result = UserModel.filter(**valid_query)
    if not result:
        raise HTTPException(status_code=404)
    return result

@user_router.post("/login", response_model=Token)
async def login_user(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = UserModel.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id})
    user.update(last_login=datetime.now())
    return Token(access_token=access_token, token_type="bearer")

@user_router.get("/me")
async def get_user(user: Annotated[UserModel, Depends(get_current_user)]):
    return user

@user_router.patch("/me")
async def update_user(user: Annotated[UserModel, Depends(get_current_user)], data: UserUpdateRequest):
    user.update(**data.model_dump())
    return user

@user_router.delete("/me")
async def delete_user(user: Annotated[UserModel, Depends(get_current_user)]):
    user.delete()
    return {"detail": "Successfully Deleted."}

