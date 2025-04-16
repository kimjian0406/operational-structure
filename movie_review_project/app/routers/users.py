# app/routers/users.py

from fastapi import APIRouter, Depends, Path
from typing import Annotated
from tortoise.expressions import Subquery

from app.models.users import User, Follow
from app.schemas.users import FollowResponse, FollowingUserResponse, FollowerUserResponse
from app.core.auth import get_current_user

user_router = APIRouter()

@user_router.post("/{user_id}/follow", status_code=200)
async def following_user(
    user: Annotated[User, Depends(get_current_user)],
    user_id: int = Path(gt=0)
) -> FollowResponse:
    follow, _ = await Follow.get_or_create(follower_id=user.id, following_id=user_id)

    if not follow.is_following:
        follow.is_following = True
        await follow.save()

    return FollowResponse(
        follower_id=follow.follower_id,
        following_id=follow.following_id,
        is_following=follow.is_following
    )


@user_router.post("/{user_id}/unfollow", status_code=200)
async def unfollowing_user(
    user: Annotated[User, Depends(get_current_user)],
    user_id: int = Path(gt=0)
) -> FollowResponse:
    follow = await Follow.filter(follower_id=user.id, following_id=user_id).first()

    if not follow:
        return FollowResponse(
            follower_id=user.id,
            following_id=user_id,
            is_following=False
        )

    if follow.is_following:
        follow.is_following = False
        await follow.save()

    return FollowResponse(
        follower_id=follow.follower_id,
        following_id=follow.following_id,
        is_following=follow.is_following
    )


@user_router.get("/me/followings", status_code=200)
async def get_my_followings(user: Annotated[User, Depends(get_current_user)]) -> list[FollowingUserResponse]:
    following_users = await User.filter(
        id__in=Subquery(Follow.filter(follower_id=user.id, is_following=True).values("following_id"))
    )

    return [
        FollowingUserResponse(
            following_id=u.id,
            username=u.username,
            profile_image_url=u.profile_image_url
        ) for u in following_users
    ]


@user_router.get("/me/followers", status_code=200)
async def get_my_followers(user: Annotated[User, Depends(get_current_user)]) -> list[FollowerUserResponse]:
    follower_users = await User.filter(
        id__in=Subquery(Follow.filter(following_id=user.id, is_following=True).values("follower_id"))
    )

    return [
        FollowerUserResponse(
            follower_id=u.id,
            username=u.username,
            profile_image_url=u.profile_image_url
        ) for u in follower_users
    ]

