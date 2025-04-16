# app/routers/replies.py

from fastapi import APIRouter, Depends, Path, HTTPException
from app.models.replies import Reply
from app.models.users import User
from app.schemas.replies import ReplyResponse
from app.utils.auth import get_current_user

reply_router = APIRouter(prefix="/replies", tags=["replies"])

@reply_router.post("", status_code=201)
async def create_reply(
    user: User = Depends(get_current_user),
    review_id: int = Path(..., title="The review id"),
    content: str = Path(..., title="Content of the reply")
) -> ReplyResponse:
    reply = await Reply.create(user_id=user.id, review_id=review_id, content=content)
    return ReplyResponse(id=reply.id, user_id=reply.user_id, review_id=reply.review_id, content=reply.content, created_at=reply.created_at)

@reply_router.get("/reviews/{review_id}", response_model=list[ReplyResponse])
async def get_replies(review_id: int = Path(..., title="The review id")) -> list[ReplyResponse]:
    replies = await Reply.filter(review_id=review_id).all()
    return [ReplyResponse(id=reply.id, user_id=reply.user_id, review_id=reply.review_id, content=reply.content, created_at=reply.created_at) for reply in replies]

@reply_router.delete("/{reply_id}", status_code=204)
async def delete_reply(
    user: User = Depends(get_current_user),
    reply_id: int = Path(..., title="The reply id")
) -> None:
    reply = await Reply.get_or_none(id=reply_id)
    if not reply:
        raise HTTPException(status_code=404, detail="Reply not found")
    if reply.user_id != user.id:
        raise HTTPException(status_code=403, detail="Only the owner can delete the reply")
    await reply.delete()

