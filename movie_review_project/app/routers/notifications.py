# app/routers/notifications.py

from fastapi import APIRouter, Depends, HTTPException
from app.models.notifications import Notification
from app.schemas.notifications import NotificationResponse
from app.models.users import User
from app.utils.auth import get_current_user

notification_router = APIRouter(prefix="/notifications", tags=["notifications"])

@notification_router.get("", response_model=list[NotificationResponse])
async def get_user_notifications(user: User = Depends(get_current_user)):
    notifications = await Notification.filter(user_id=user.id).all()
    return notifications

@notification_router.patch("/{notification_id}/read", status_code=204)
async def mark_notification_as_read(
    notification_id: int,
    user: User = Depends(get_current_user)
):
    notification = await Notification.get_or_none(id=notification_id, user_id=user.id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification.is_read = True
    await notification.save()
