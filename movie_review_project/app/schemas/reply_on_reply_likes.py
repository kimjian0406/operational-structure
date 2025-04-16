from pydantic import BaseModel
from datetime import datetime

class ReplyOnReplyLikeResponse(BaseModel):
    id: int
    user_id: int
    reply_on_reply_id: int
    created_at: datetime
