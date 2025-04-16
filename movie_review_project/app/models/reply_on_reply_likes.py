# app/models/reply_on_reply_likes.py

from tortoise import Model, fields
from app.models.base import BaseModel

class ReplyOnReplyLike(BaseModel, Model):
    user = fields.ForeignKeyField("models.User", related_name="reply_on_reply_likes", on_delete=fields.CASCADE)
    reply_on_reply = fields.ForeignKeyField("models.ReplyOnReply", related_name="likes", on_delete=fields.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reply_on_reply_likes"

