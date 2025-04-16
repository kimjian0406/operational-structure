# app/models/replies.py

from tortoise import Model, fields
from app.models.base import BaseModel

class Reply(BaseModel, Model):
    user = fields.ForeignKeyField("models.User", related_name="replies", on_delete=fields.CASCADE)
    review = fields.ForeignKeyField("models.Review", related_name="replies", on_delete=fields.CASCADE)
    content = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "replies"

