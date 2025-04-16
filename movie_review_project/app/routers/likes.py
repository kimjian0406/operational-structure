# app/routers/likes.py

from typing import Annotated
from fastapi import APIRouter, Depends, Path
from app.models.likes import ReviewLike
from app.models.users import User
from app.schemas.likes import ReviewLikeResponse, ReviewLikeCountResponse, ReviewIsLikedResponse
from app.routers.reviews import review_router
from app.utils.auth import get_current_user

like_router = APIRouter(prefix="/likes", tags=["likes"])

@like_router.post("/reviews/{review_id}/like", status_code=200)
async def like_review(
    user: Annotated[User, Depends(get_current_user)],
    review_id: int = Path(gt=0)
) -> ReviewLikeResponse:
    review_like, _ = await ReviewLike.get_or_create(user_id=user.id, review_id=review_id)

    if not review_like.is_liked:
        review_like.is_liked = True
        await review_like.save()

    return ReviewLikeResponse(
        id=review_like.id,
        user_id=review_like.user_id,
        review_id=review_like.review_id,
        is_liked=review_like.is_liked
    )

@like_router.post("/reviews/{review_id}/unlike", status_code=200)
async def unlike_review(
    user: Annotated[User, Depends(get_current_user)],
    review_id: int = Path(gt=0)
) -> ReviewLikeResponse:
    review_like = await ReviewLike.get_or_none(user_id=user.id, review_id=review_id)

    if review_like is None:
        return ReviewLikeResponse(
            user_id=user.id,
            review_id=review_id,
            is_liked=False
        )

    if review_like.is_liked:
        review_like.is_liked = False
        await review_like.save()

    return ReviewLikeResponse(
        id=review_like.id,
        user_id=review_like.user_id,
        review_id=review_like.review_id,
        is_liked=review_like.is_liked
    )

@like_router.post("/reviews/{review_id}/like", status_code=200)
async def like_review(request: Request, review_id: int = Path(gt=0)) -> ReviewLikeResponse:
    user_id = request.state.user.id
    like, _ = await ReviewLike.get_or_create(user_id=user_id, review_id=review_id)

    if not like.is_liked:
        like.is_liked = True
        await like.save()

    return ReviewLikeResponse(
        id=like.id,
        user_id=like.user_id,
        review_id=like.review_id,
        is_liked=like.is_liked,
    )


@like_router.post("/reviews/{review_id}/unlike", status_code=200)
async def unlike_review(request: Request, review_id: int = Path(gt=0)) -> ReviewLikeResponse:
    user_id = request.state.user.id
    like = await ReviewLike.get_or_none(user_id=user_id, review_id=review_id)

    if not like:
        return ReviewLikeResponse(
            id=None,
            user_id=user_id,
            review_id=review_id,
            is_liked=False,
        )

    if like.is_liked:
        like.is_liked = False
        await like.save()

    return ReviewLikeResponse(
        id=like.id,
        user_id=like.user_id,
        review_id=like.review_id,
        is_liked=like.is_liked,
    )
# app/routers/likes.py

from fastapi import APIRouter, Depends, Path
from typing import Annotated

from app.models.likes import MovieReaction, ReactionTypeEnum
from app.models.movies import Movie
from app.models.users import User
from app.schemas.likes import MovieReactionResponse, MovieReactionCountResponse
from app.core.auth import get_current_user

like_router = APIRouter()

@like_router.post("/movies/{movie_id}/like", status_code=200)
async def like_movie(
    user: Annotated[User, Depends(get_current_user)],
    movie_id: int = Path(gt=0)
) -> MovieReactionResponse:
    reaction, _ = await MovieReaction.get_or_create(user_id=user.id, movie_id=movie_id)

    if reaction.type != ReactionTypeEnum.LIKE:
        reaction.type = ReactionTypeEnum.LIKE
        await reaction.save()

    return MovieReactionResponse(
        id=reaction.id,
        user_id=reaction.user_id,
        movie_id=reaction.movie_id,
        type=reaction.type
    )


@like_router.post("/movies/{movie_id}/dislike", status_code=200)
async def dislike_movie(
    user: Annotated[User, Depends(get_current_user)],
    movie_id: int = Path(gt=0)
) -> MovieReactionResponse:
    reaction, _ = await MovieReaction.get_or_create(user_id=user.id, movie_id=movie_id)

    if reaction.type != ReactionTypeEnum.DISLIKE:
        reaction.type = ReactionTypeEnum.DISLIKE
        await reaction.save()

    return MovieReactionResponse(
        id=reaction.id,
        user_id=reaction.user_id,
        movie_id=reaction.movie_id,
        type=reaction.type
    )


@like_router.get("/movies/{movie_id}/reaction_count", status_code=200)
async def get_movie_reaction_count(movie_id: int = Path(gt=0)) -> MovieReactionCountResponse:
    like_count = await MovieReaction.filter(movie_id=movie_id, type=ReactionTypeEnum.LIKE).count()
    dislike_count = await MovieReaction.filter(movie_id=movie_id, type=ReactionTypeEnum.DISLIKE).count()

    return MovieReactionCountResponse(
        movie_id=movie_id,
        like_count=like_count,
        dislike_count=dislike_count
    )

