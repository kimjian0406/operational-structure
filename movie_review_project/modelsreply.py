from tortoise import fields
from tortoise.models import Model


class Reply(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="replies", on_delete=fields.CASCADE)
    review = fields.ForeignKeyField("models.Review", related_name="replies", on_delete=fields.CASCADE)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "reply"

    def __str__(self):
        return f"Reply {self.id} by User {self.user_id}"
	
