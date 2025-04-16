from pydantic import BaseModel

class ReplyLikeCreate(BaseModel):
    reply_id: int  # 댓글 ID
    user_id: int   # 사용자 ID

class ReplyLikeOut(BaseModel):
    id: int
    reply_id: int
    user_id: int

    class Config:
        orm_mode = True  # ORM 모델과 호환되도록 설정

