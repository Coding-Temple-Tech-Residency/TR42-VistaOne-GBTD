from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user_profiles import UserProfile


class UserProfilesService:

    @staticmethod
    async def get_by_auth_user_id(db: AsyncSession, auth_user_id: str):
        result = await db.execute(
            select(UserProfile).where(UserProfile.auth_user_id == auth_user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, auth_user_id: str, role: str):
        profile = UserProfile(auth_user_id=auth_user_id, role=role)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
        return profile
