# app/models/users.py

from tortoise import fields
from tortoise.models import Model
from app.models.enums import GenderEnum
from app.models.base import BaseModel

class User(BaseModel, Model):
    username = fields.CharField(unique=True, max_length=50, index=True)  
    hashed_password = fields.CharField(max_length=128)
    age = fields.IntField()
    gender = fields.CharEnumField(GenderEnum)
    profile_image_url = fields.CharField(max_length=255, null=True)  # ✅ 추가된 필드
    last_login = fields.DatetimeField(null=True)

    class Meta:
        table = 'users'

