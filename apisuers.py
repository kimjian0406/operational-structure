from app.schemas.users import UserUpdateRequest
from fastapi import HTTPException

@router.patch("/me")
def update_me(
    current_user: Annotated[UserModel, Depends(get_current_user)],
    data: UserUpdateRequest,
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    current_user.update(**data.model_dump())
    return current_user


@router.delete("/me")
def delete_me(current_user: Annotated[UserModel, Depends(get_current_user)]):
    current_user.delete()
    return {"detail": "Successfully deleted."}

