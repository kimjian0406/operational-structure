# app/schemas/notifications.py

from pydantic import BaseModel
from datetime import datetime

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    type: str
    message: str
    created_at: datetime

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    type: str
    message: str
    is_read: bool  # ✅ 읽음 여부
    created_at: datetime
