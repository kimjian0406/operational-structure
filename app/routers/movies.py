from typing import Annotated
from fastapi import Path, HTTPException, Query, APIRouter

from app.models.movies import MovieModel
from app.schemas.movies import MovieResponse, CreateMovieRequest, MovieSearchParams, MovieUpdateRequest

movie_router = APIRouter(prefix="/movies", tags=["movies"])

@movie_router.post("", response_model=MovieResponse, status_code=201)
async def create_movie(data: CreateMovieRequest):
    return MovieModel.create(**data.model_dump())

@movie_router.get("", response_model=list[MovieResponse], status_code=200)
async def get_movies(query_params: Annotated[MovieSearchParams, Query()]):
    filters = {k: v for k, v in query_params.model_dump().items() if v is not None}
    return MovieModel.filter(**filters) if filters else MovieModel.all()

@movie_router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if not movie:
        raise HTTPException(status_code=404)
    return movie

@movie_router.patch("/{movie_id}", response_model=MovieResponse)
async def update_movie(data: MovieUpdateRequest, movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if not movie:
        raise HTTPException(status_code=404)
    movie.update(**data.model_dump())
    return movie

@movie_router.delete("/{movie_id}", status_code=204)
async def delete_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if not movie:
        raise HTTPException(status_code=404)
    movie.delete()

# app/routers/movies.py

from typing import Annotated
from fastapi import Path, HTTPException, Query, APIRouter, Depends
from app.models.movies import MovieModel
from app.schemas.movies import MovieResponse, CreateMovieRequest, MovieSearchParams, MovieUpdateRequest
from app.models.users import UserModel
from app.utils.jwt import get_current_user

movie_router = APIRouter(prefix="/movies", tags=["movies"])

@movie_router.post('', response_model=MovieResponse, status_code=201)
async def create_movie(
    data: CreateMovieRequest,
    user: Annotated[UserModel, Depends(get_current_user)],
):
    movie = MovieModel.create(**data.model_dump())
    return movie

@movie_router.get('', response_model=list[MovieResponse], status_code=200)
async def get_movies(query_params: Annotated[MovieSearchParams, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}
    if valid_query:
        return MovieModel.filter(**valid_query)
    return MovieModel.all()

@movie_router.get('/{movie_id}', response_model=MovieResponse, status_code=200)
async def get_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    return movie

@movie_router.patch('/{movie_id}', response_model=MovieResponse, status_code=200)
async def edit_movie(
    data: MovieUpdateRequest,
    movie_id: int = Path(gt=0),
    user: Annotated[UserModel, Depends(get_current_user)],
):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.update(**data.model_dump())
    return movie

@movie_router.delete('/{movie_id}', status_code=204)
async def delete_movie(
    movie_id: int = Path(gt=0),
    user: Annotated[UserModel, Depends(get_current_user)],
):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.delete()
    return

