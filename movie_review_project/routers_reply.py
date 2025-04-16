from fastapi import APIRouter, Depends, HTTPException, status
from tortoise.exceptions import DoesNotExist

from models import Reply
from schemas_reply import ReplyCreateSchema, ReplyUpdateSchema, ReplyResponseSchema
from dependencies import get_current_user
from models import User

router = APIRouter()


@router.post("/replies/", response_model=ReplyResponseSchema)
async def create_reply(reply_data: ReplyCreateSchema, current_user: User = Depends(get_current_user)):
    reply = await Reply.create(
        user=current_user,
        review_id=reply_data.review_id,
        content=reply_data.content
    )
    return await ReplyResponseSchema.from_tortoise_orm(reply)


@router.put("/replies/{reply_id}", response_model=ReplyResponseSchema)
async def update_reply(reply_id: int, reply_data: ReplyUpdateSchema, current_user: User = Depends(get_current_user)):
    try:
        reply = await Reply.get(id=reply_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Reply not found")

    if reply.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this reply")

    reply.content = reply_data.content
    await reply.save()
    return await ReplyResponseSchema.from_tortoise_orm(reply)


@router.delete("/replies/{reply_id}")
async def delete_reply(reply_id: int, current_user: User = Depends(get_current_user)):
    try:
        reply = await Reply.get(id=reply_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Reply not found")

    if reply.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this reply")

    await reply.delete()
    return {"message": "Reply deleted"}


@router.get("/reviews/{review_id}/replies/", response_model=list[ReplyResponseSchema])
async def get_replies_for_review(review_id: int):
    replies = await Reply.filter(review_id=review_id).order_by("-created_at")
    return replies

