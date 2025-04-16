# app/models/reply_on_replies.py

from tortoise import Model, fields
from app.models.base import BaseModel

class ReplyOnReply(BaseModel, Model):
    user = fields.ForeignKeyField("models.User", related_name="reply_on_replies", on_delete=fields.CASCADE)
    parent_reply = fields.ForeignKeyField("models.Reply", related_name="reply_on_replies", on_delete=fields.CASCADE)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reply_on_replies"

