from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import ReplyLike
from schemas import ReplyLikeCreate, ReplyLikeOut
from db import get_db  # DB 세션을 가져오는 의존성

router = APIRouter()

@router.post("/", response_model=ReplyLikeOut)
def create_reply_like(reply_like: ReplyLikeCreate, db: Session = Depends(get_db)):
    # 댓글에 좋아요 추가
    db_reply_like = ReplyLike(
        reply_id=reply_like.reply_id,
        user_id=reply_like.user_id
    )
    db.add(db_reply_like)
    db.commit()
    db.refresh(db_reply_like)
    return db_reply_like

@router.get("/", response_model=List[ReplyLikeOut])
def get_reply_likes(db: Session = Depends(get_db)):
    # 모든 댓글 좋아요 조회
    reply_likes = db.query(ReplyLike).all()
    return reply_likes

@router.delete("/{reply_like_id}", response_model=ReplyLikeOut)
def delete_reply_like(reply_like_id: int, db: Session = Depends(get_db)):
    # 댓글 좋아요 삭제
    db_reply_like = db.query(ReplyLike).filter(ReplyLike.id == reply_like_id).first()
    if db_reply_like is None:
        raise HTTPException(status_code=404, detail="Reply Like not found")
    
    db.delete(db_reply_like)
    db.commit()
    return db_reply_like

class Reply(Base):
    __tablename__ = "replies"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    # 댓글에 대한 좋아요 연관
    likes = relationship("ReplyLike", back_populates="reply")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # 사용자가 좋아요 한 댓글
    likes = relationship("ReplyLike", back_populates="user")

