# app/schemas/replies.py

from pydantic import BaseModel
from datetime import datetime

class ReplyResponse(BaseModel):
    id: int
    user_id: int
    review_id: int
    content: str
    created_at: datetime

