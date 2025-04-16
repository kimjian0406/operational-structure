# app/routers/reply_likes.py

from fastapi import APIRouter, Depends, HTTPException, Path
from app.models.reply_likes import ReplyLike
from app.models.replies import Reply
from app.models.users import User
from app.schemas.reply_likes import ReplyLikeResponse
from app.utils.auth import get_current_user

reply_like_router = APIRouter(prefix="/reply_likes", tags=["reply_likes"])

@reply_like_router.post("", status_code=201)
async def create_reply_like(
    user: User = Depends(get_current_user),
    reply_id: int = Path(..., title="The reply id")
) -> ReplyLikeResponse:
    # 댓글 존재 확인
    reply = await Reply.get_or_none(id=reply_id)
    if not reply:
        raise HTTPException(status_code=404, detail="Reply not found")

    # 이미 좋아요를 눌렀는지 확인
    existing_like = await ReplyLike.filter(user_id=user.id, reply_id=reply_id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this reply")

    # 좋아요 추가
    reply_like = await ReplyLike.create(user_id=user.id, reply_id=reply_id)
    return ReplyLikeResponse(id=reply_like.id, user_id=reply_like.user_id, reply_id=reply_like.reply_id, created_at=reply_like.created_at)

@reply_like_router.delete("/{reply_like_id}", status_code=204)
async def delete_reply_like(
    user: User = Depends(get_current_user),
    reply_like_id: int = Path(..., title="The reply like id")
) -> None:
    reply_like = await ReplyLike.get_or_none(id=reply_like_id)
    if not reply_like:
        raise HTTPException(status_code=404, detail="ReplyLike not found")
    if reply_like.user_id != user.id:
        raise HTTPException(status_code=403, detail="Only the owner can delete the like")
    await reply_like.delete()

@reply_like_router.get("/replies/{reply_id}", response_model=list[ReplyLikeResponse])
async def get_reply_likes(reply_id: int = Path(..., title="The reply id")) -> list[ReplyLikeResponse]:
    reply_likes = await ReplyLike.filter(reply_id=reply_id).all()
    return [ReplyLikeResponse(id=like.id, user_id=like.user_id, reply_id=like.reply_id, created_at=like.created_at) for like in reply_likes]

