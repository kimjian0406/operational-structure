from fastapi import APIRouter, Depends, HTTPException, Path
from app.models.reply_on_reply_likes import ReplyOnReplyLike
from app.models.reply_on_replies import ReplyOnReply
from app.models.users import User
from app.schemas.reply_on_reply_likes import ReplyOnReplyLikeResponse
from app.utils.auth import get_current_user

reply_on_reply_like_router = APIRouter(prefix="/reply_on_reply_likes", tags=["reply_on_reply_likes"])

@reply_on_reply_like_router.post("", status_code=201)
async def create_reply_on_reply_like(
    user: User = Depends(get_current_user),
    reply_on_reply_id: int = Path(..., title="The reply on reply id")
) -> ReplyOnReplyLikeResponse:
    # 답글 존재 확인
    reply_on_reply = await ReplyOnReply.get_or_none(id=reply_on_reply_id)
    if not reply_on_reply:
        raise HTTPException(status_code=404, detail="ReplyOnReply not found")

    # 좋아요 추가
    reply_on_reply_like = await ReplyOnReplyLike.create(user_id=user.id, reply_on_reply_id=reply_on_reply_id)
    return ReplyOnReplyLikeResponse(id=reply_on_reply_like.id, user_id=reply_on_reply_like.user_id, reply_on_reply_id=reply_on_reply_like.reply_on_reply_id, created_at=reply_on_reply_like.created_at)

@reply_on_reply_like_router.delete("/{reply_on_reply_like_id}", status_code=204)
async def delete_reply_on_reply_like(
    user: User = Depends(get_current_user),
    reply_on_reply_like_id: int = Path(..., title="The reply on reply like id")
) -> None:
    reply_on_reply_like = await ReplyOnReplyLike.get_or_none(id=reply_on_reply_like_id)
    if not reply_on_reply_like:
        raise HTTPException(status_code=404, detail="ReplyOnReplyLike not found")
    if reply_on_reply_like.user_id != user.id:
        raise HTTPException(status_code=403, detail="Only the owner can delete the like")
    await reply_on_reply_like.delete()
