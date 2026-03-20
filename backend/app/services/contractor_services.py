from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.contractors import Contractor


class ContractorService:

    @staticmethod
    async def list(db: AsyncSession):
        result = await db.execute(select(Contractor))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, contractor_id: int):
        result = await db.execute(
            select(Contractor).where(Contractor.category_id == contractor_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, user, data: dict):
        data["auth_user_id"] = user.id
        contractor = Contractor(**data)
        db.add(contractor)
        await db.commit()
        await db.refresh(contractor)
        return contractor

    @staticmethod
    async def update(db: AsyncSession, contractor: Contractor, updates: dict):
        for key, value in updates.items():
            setattr(contractor, key, value)
        await db.commit()
        await db.refresh(contractor)
        return contractor

    @staticmethod
    async def delete(db: AsyncSession, contractor: Contractor):
        await db.delete(contractor)
        await db.commit()
