# app/schemas/likes.py

from pydantic import BaseModel

class ReviewLikeResponse(BaseModel):
    id: int
    user_id: int
    review_id: int
    is_liked: bool

class ReviewLikeCountResponse(BaseModel):
    review_id: int
    like_count: int

class ReviewIsLikedResponse(BaseModel):
    review_id: int
    user_id: int
    is_liked: bool

