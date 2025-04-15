# app/crud/users.py
from app.models.users import User
from app.schemas.users import UserCreate
from app.core.security import create_access_token
from passlib.context import CryptContext
from datetime import timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(username: str):
    return User.get_or_none(username=username)

def create_user(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user_obj = User.create(username=user.username, email=user.email, hashed_password=hashed_password)
    return user_obj

def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_access_token_for_user(user: User):
    data = {"sub": user.username}
    return create_access_token(data)

