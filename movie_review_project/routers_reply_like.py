from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import reply_like as crud_reply_like
from schemas import ReplyLikeCreate, ReplyLikeOut
from db import get_db

router = APIRouter()

# 댓글에 좋아요 추가
@router.post("/", response_model=ReplyLikeOut)
def create_reply_like(reply_like: ReplyLikeCreate, db: Session = Depends(get_db)):
    return crud_reply_like.create_reply_like(db=db, reply_like=reply_like)

# 댓글 좋아요 삭제
@router.delete("/{reply_like_id}", response_model=ReplyLikeOut)
def delete_reply_like(reply_like_id: int, db: Session = Depends(get_db)):
    return crud_reply_like.delete_reply_like(db=db, reply_like_id=reply_like_id)

