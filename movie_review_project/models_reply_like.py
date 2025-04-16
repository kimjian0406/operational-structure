from tortoise import fields, models
from models import User, Reply

class ReplyLike(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="reply_likes")
    reply = fields.ForeignKeyField("models.Reply", related_name="likes")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reply_likes"
        unique_together = ("user", "reply")

