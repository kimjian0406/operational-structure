import asyncio
from app.models.movies import Movie
from app.services.tmdb_service import fetch_popular_movies
from tortoise import Tortoise, run_async
from app.core.config import TORTOISE_ORM  # DB 설정 가져오기

async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

async def fetch_and_save():
    await init()
    data = fetch_popular_movies()

    for item in data:
        await Movie.get_or_create(
            title=item["title"],
            defaults={
                "overview": item.get("overview"),
                "release_date": item.get("release_date"),
                "popularity": item.get("popularity"),
                "poster_path": item.get("poster_path")
            }
        )

    await Tortoise.close_connections()

if __name__ == "__main__":
    run_async(fetch_and_save())

