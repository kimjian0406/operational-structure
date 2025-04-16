# app/models/users.py

class Follow(BaseModel, Model):
    follower = fields.ForeignKeyField('models.User', related_name='followers')
    following = fields.ForeignKeyField('models.User', related_name='followings')
    is_following = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'follows'
        unique_together = (('follower', 'following'),)

