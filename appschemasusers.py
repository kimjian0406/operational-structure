from typing import Optional
...
class UserResponse(BaseModel):
    id: int
    username: str
    age: int
    gender: GenderEnum
    profile_image_url: Optional[str] = None  # ✅ 추가

    ...

