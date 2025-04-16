from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas_reply_like
from .. import crud, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas_reply_like.ReplyLikeOut)
def create_reply_like(
    reply_like: schemas_reply_like.ReplyLikeCreate, db: Session = Depends(get_db)
):
    # 댓글이 존재하는지 체크
    reply = db.query(models.Reply).filter(models.Reply.id == reply_like.reply_id).first()
    if not reply:
        raise HTTPException(status_code=404, detail="Reply not found")

    # 댓글 좋아요 추가
    db_reply_like = crud.create_reply_like(db=db, reply_like=reply_like)
    return db_reply_like

@router.get("/", response_model=List[schemas_reply_like.ReplyLikeOut])
def get_reply_likes(db: Session = Depends(get_db)):
    # 모든 댓글 좋아요 반환
    return crud.get_reply_likes(db=db)

@router.delete("/{reply_like_id}", response_model=schemas_reply_like.ReplyLikeOut)
def delete_reply_like(
    reply_like_id: int, db: Session = Depends(get_db)
):
    db_reply_like = crud.delete_reply_like(db=db, reply_like_id=reply_like_id)
    if not db_reply_like:
        raise HTTPException(status_code=404, detail="ReplyLike not found")
    return db_reply_like

