# app/schemas/reply_likes.py

from pydantic import BaseModel
from datetime import datetime

class ReplyLikeResponse(BaseModel):
    id: int
    user_id: int
    reply_id: int
    created_at: datetime

