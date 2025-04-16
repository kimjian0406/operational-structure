# app/schemas/reply_on_replies.py

from pydantic import BaseModel
from datetime import datetime

class ReplyOnReplyResponse(BaseModel):
    id: int
    user_id: int
    parent_reply_id: int
    content: str
    created_at: datetime

