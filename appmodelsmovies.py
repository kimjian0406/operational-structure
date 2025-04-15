# app/models/movies.py

from tortoise import fields
from tortoise.models import Model
from app.models.enums import GenreEnum
from app.models.base import BaseModel

class Movie(BaseModel, Model):
    title = fields.CharField(max_length=255)
    plot = fields.TextField()
    cast = fields.JSONField()
    playtime = fields.IntField()
    genre = fields.CharEnumField(GenreEnum)
    poster_image_url = fields.CharField(max_length=255, null=True)  # ✅ 추가된 필드

    class Meta:
        table = "movies"

