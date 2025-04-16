from pydantic import BaseModel
from datetime import datetime


class ReplyCreateSchema(BaseModel):
    review_id: int
    content: str


class ReplyUpdateSchema(BaseModel):
    content: str


class ReplyResponseSchema(BaseModel):
    id: int
    user_id: int
    review_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
	
