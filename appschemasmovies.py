from typing import Optional
...
class MovieResponse(BaseModel):
    id: int
    title: str
    playtime: int
    plot: str
    cast: dict[str, Any]
    genre: GenreEnum
    poster_image_url: Optional[str] = None  # ✅ 추가

    ...

