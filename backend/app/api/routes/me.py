from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return {
        "auth_user_id": user.id,
        "email": user.email,
        "role": user.role
    }
