from pydantic import BaseModel
from datetime import datetime

class ReplyLikeCreate(BaseModel):
    reply_id: int

class ReplyLikeOut(BaseModel):
    id: int
    reply_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

