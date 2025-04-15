# app/routers/protected.py
from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/protected")
async def get_protected_data(current_user: dict = Depends(get_current_user)):
    return {"message": "This is protected data", "user": current_user}

