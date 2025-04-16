from sqlalchemy.orm import Session
from . import models, schemas_reply_like

# 댓글 좋아요 생성
def create_reply_like(db: Session, reply_like: schemas_reply_like.ReplyLikeCreate):
    db_reply_like = models.ReplyLike(
        user_id=reply_like.user_id,
        reply_id=reply_like.reply_id
    )
    db.add(db_reply_like)
    db.commit()
    db.refresh(db_reply_like)
    return db_reply_like

# 모든 댓글 좋아요 조회
def get_reply_likes(db: Session):
    return db.query(models.ReplyLike).all()

# 댓글 좋아요 삭제
def delete_reply_like(db: Session, reply_like_id: int):
    db_reply_like = db.query(models.ReplyLike).filter(models.ReplyLike.id == reply_like_id).first()
    if db_reply_like:
        db.delete(db_reply_like)
        db.commit()
    return db_reply_like

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import ReplyLike
from schemas import ReplyLikeCreate, ReplyLikeOut

# 댓글에 좋아요 추가
def create_reply_like(db: Session, reply_like: ReplyLikeCreate):
    # 이미 해당 댓글에 좋아요가 있는지 확인
    db_reply_like = db.query(ReplyLike).filter(ReplyLike.reply_id == reply_like.reply_id, ReplyLike.user_id == reply_like.user_id).first()
    if db_reply_like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already liked this reply"
        )
    
    # 새로 좋아요 추가
    new_reply_like = ReplyLike(reply_id=reply_like.reply_id, user_id=reply_like.user_id)
    db.add(new_reply_like)
    db.commit()
    db.refresh(new_reply_like)
    return new_reply_like

# 댓글 좋아요 삭제
def delete_reply_like(db: Session, reply_like_id: int):
    db_reply_like = db.query(ReplyLike).filter(ReplyLike.id == reply_like_id).first()
    if not db_reply_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ReplyLike not found"
        )
    
    db.delete(db_reply_like)
    db.commit()
    return db_reply_like

