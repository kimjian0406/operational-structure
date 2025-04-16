from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class ReplyLike(Base):
    __tablename__ = "reply_likes"
    
    id = Column(Integer, primary_key=True, index=True)
    reply_id = Column(Integer, ForeignKey("replies.id"), index=True)  # 댓글 ID
    user_id = Column(Integer, ForeignKey("users.id"), index=True)     # 사용자 ID

    reply = relationship("Reply", back_populates="likes")
    user = relationship("User", back_populates="likes")

