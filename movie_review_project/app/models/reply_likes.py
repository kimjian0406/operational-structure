# app/models/reply_likes.py

from tortoise import Model, fields
from app.models.base import BaseModel

class ReplyLike(BaseModel, Model):
    user = fields.ForeignKeyField("models.User", related_name="reply_likes", on_delete=fields.CASCADE)
    reply = fields.ForeignKeyField("models.Reply", related_name="reply_likes", on_delete=fields.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reply_likes"

