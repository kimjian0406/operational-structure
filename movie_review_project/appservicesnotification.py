# app/services/notification.py

from app.routers.notifications_ws import active_connections
from app.models.notifications import Notification

async def create_notification(user: User, type: str, message: str):
    notification = await Notification.create(user=user, type=type, message=message)

    # ✅ 실시간 전송
    ws = active_connections.get(user.id)
    if ws:
        await ws.send_json({
            "id": notification.id,
            "type": type,
            "message": message,
            "created_at": str(notification.created_at),
        })

    return notification

