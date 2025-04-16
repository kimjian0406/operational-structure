class Movie(BaseModel, Model):
    title = fields.CharField(max_length=255)
    overview = fields.TextField(null=True)
    release_date = fields.DateField(null=True)
    popularity = fields.FloatField(null=True)
    poster_path = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "movies"

