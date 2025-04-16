# app/models/notifications.py

class Notification(BaseModel, Model):
    user = fields.ForeignKeyField("models.User", related_name="notifications", on_delete=fields.CASCADE)
    type = fields.CharField(max_length=100)
    message = fields.TextField()
    is_read = fields.BooleanField(default=False)  # ✅ 읽음 여부 필드
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "notifications"

