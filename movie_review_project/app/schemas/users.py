# app/schemas/users.py

from pydantic import BaseModel

class FollowResponse(BaseModel):
    follower_id: int
    following_id: int
    is_following: bool

class FollowingUserResponse(BaseModel):
    following_id: int
    username: str
    profile_image_url: str | None = None

class FollowerUserResponse(BaseModel):
    follower_id: int
    username: str
    profile_image_url: str | None = None

