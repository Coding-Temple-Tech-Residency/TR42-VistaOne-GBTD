
from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.auth.rbac import require_role

router = APIRouter()

@router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return {
        "user_id": user["user_id"],
        "email": user["email"],
        "role": user["role"],
    }

@router.get("/admin-only")
async def admin_only(user = Depends(get_current_user)):
    require_role("admin")(user)
    return {"message": "Welcome admin", "user_id": user["user_id"]}
