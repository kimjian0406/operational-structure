from fastapi import UploadFile, Path, HTTPException
from app.utils.file import upload_file, delete_file, validate_image_extension

@movie_router.post("/{movie_id}/poster_image", response_model=MovieResponse, status_code=201)
async def register_poster_image(image: UploadFile, movie_id: int = Path(gt=0)):
    validate_image_extension(image)

    movie = await Movie.get_or_none(id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    prev_image_url = movie.poster_image_url
    try:
        image_url = await upload_file(image, "movies/poster_images")
        movie.poster_image_url = image_url
        await movie.save()

        if prev_image_url is not None:
            delete_file(prev_image_url)

        return movie
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

