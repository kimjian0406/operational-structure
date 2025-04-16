# app/routers/reply_on_replies.py

from fastapi import APIRouter, Depends, HTTPException, Path
from app.models.reply_on_replies import ReplyOnReply
from app.models.replies import Reply
from app.models.users import User
from app.schemas.reply_on_replies import ReplyOnReplyResponse
from app.utils.auth import get_current_user

reply_on_reply_router = APIRouter(prefix="/reply_on_replies", tags=["reply_on_replies"])

@reply_on_reply_router.post("", status_code=201)
async def create_reply_on_reply(
    user: User = Depends(get_current_user),
    parent_reply_id: int = Path(..., title="The parent reply id"),
    content: str
) -> ReplyOnReplyResponse:
    # 부모 댓글 존재 확인
    parent_reply = await Reply.get_or_none(id=parent_reply_id)
    if not parent_reply:
        raise HTTPException(status_code=404, detail="Parent reply not found")

    # 답글 추가
    reply_on_reply = await ReplyOnReply.create(user_id=user.id, parent_reply_id=parent_reply_id, content=content)
    return ReplyOnReplyResponse(id=reply_on_reply.id, user_id=reply_on_reply.user_id, parent_reply_id=reply_on_reply.parent_reply_id, content=reply_on_reply.content, created_at=reply_on_reply.created_at)

@reply_on_reply_router.delete("/{reply_on_reply_id}", status_code=204)
async def delete_reply_on_reply(
    user: User = Depends(get_current_user),
    reply_on_reply_id: int = Path(..., title="The reply on reply id")
) -> None:
    reply_on_reply = await ReplyOnReply.get_or_none(id=reply_on_reply_id)
    if not reply_on_reply:
        raise HTTPException(status_code=404, detail="ReplyOnReply not found")
    if reply_on_reply.user_id != user.id:
        raise HTTPException(status_code=403, detail="Only the owner can delete the reply")
    await reply_on_reply.delete()

@reply_on_reply_router.get("/replies/{parent_reply_id}", response_model=list[ReplyOnReplyResponse])
async def get_reply_on_replies(parent_reply_id: int = Path(..., title="The parent reply id")) -> list[ReplyOnReplyResponse]:
    reply_on_replies = await ReplyOnReply.filter(parent_reply_id=parent_reply_id).all()
    return [ReplyOnReplyResponse(id=reply.id, user_id=reply.user_id, parent_reply_id=reply.parent_reply_id, content=reply.content, created_at=reply.created_at) for reply in reply_on_replies]

# app/routers/reply_on_replies.py

from fastapi import APIRouter, Depends, HTTPException, Path
from app.models.reply_on_replies import ReplyOnReply
from app.models.notifications import Notification
from app.models.replies import Reply
from app.models.users import User
from app.schemas.replies import ReplyResponse
from app.utils.auth import get_current_user

reply_on_reply_router = APIRouter(prefix="/reply_on_replies", tags=["reply_on_replies"])

@reply_on_reply_router.post("", status_code=201)
async def create_reply_on_reply(
    user: User = Depends(get_current_user),
    reply_on_reply_id: int = Path(..., title="The reply on reply id"),
    message: str = Path(..., title="The reply message")
) -> ReplyResponse:
    # 원래 댓글에 대한 답글을 가져옴
    reply_on_reply = await ReplyOnReply.get_or_none(id=reply_on_reply_id)
    if not reply_on_reply:
        raise HTTPException(status_code=404, detail="ReplyOnReply not found")

    # 답글 작성
    reply = await Reply.create(user_id=user.id, message=message, reply_on_reply_id=reply_on_reply_id)
    
    # 댓글 작성자에게 알림 생성
    if reply_on_reply.user.id != user.id:  # 자신에게 답글을 달았을 때는 알림을 보내지 않음
        notification = await Notification.create(
            user_id=reply_on_reply.user.id,
            type="reply",
            message=f"Your comment received a reply from {user.username}: {message}"
        )
    
    return ReplyResponse(id=reply.id, user_id=reply.user_id, message=reply.message, created_at=reply.created_at)

