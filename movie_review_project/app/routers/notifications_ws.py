# app/routers/notifications_ws.py
from fastapi import WebSocket, WebSocketDisconnect, Depends, APIRouter
from app.models.users import User
from app.core.auth import get_current_user_by_token

ws_router = APIRouter()

active_connections = {}

@ws_router.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # ✅ 토큰에서 사용자 정보 파싱
    token = websocket.headers.get("Authorization", "").replace("Bearer ", "")
    user = await get_current_user_by_token(token)

    if user:
        active_connections[user.id] = websocket
    else:
        await websocket.close()

    try:
        while True:
            await websocket.receive_text()  # 클라이언트로부터 ping 등 받을 수 있음
    except WebSocketDisconnect:
        if user and user.id in active_connections:
            del active_connections[user.id]

