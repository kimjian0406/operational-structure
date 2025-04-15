from fastapi import UploadFile, Depends, HTTPException
from app.utils.file import upload_file, delete_file, validate_image_extension
from app.dependencies.auth import get_current_user

@user_router.post("/me/profile_image", response_model=UserResponse, status_code=200)
async def register_profile_image(
    image: UploadFile, user: Annotated[User, Depends(get_current_user)]
):
    validate_image_extension(image)
    prev_image_url = user.profile_image_url
    try:
        image_url = await upload_file(image, "users/profile_images")
        user.profile_image_url = image_url
        await user.save()

        if prev_image_url is not None:
            delete_file(prev_image_url)

        return UserResponse(
            id=user.id,
            username=user.username,
            age=user.age,
            gender=user.gender,
            profile_image_url=user.profile_image_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

