from fastapi import APIRouter, Depends
from app.db.models.user_profile import UserProfilesService
from app.dependencies import require_admin
from app.db.db import get_db
from backend.app.db.schemas.users_profile import UserProfileCreate, UserProfileResponse

router = APIRouter(prefix="/user-profiles", tags=["User Profiles"])


@router.post("/", response_model=UserProfileResponse)
async def create_user_profile(
    data: UserProfileCreate,
    user=Depends(require_admin),
    db=Depends(get_db)
):
    return await UserProfilesService.create(db, data.auth_user_id, data.role)
