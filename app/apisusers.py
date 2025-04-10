from typing import Annotated
from fastapi import Depends
from app.utils.auth import get_current_user
from app.models.users import UserModel

@router.get("/me")
def get_me(current_user: Annotated[UserModel, Depends(get_current_user)]):
    return current_user

