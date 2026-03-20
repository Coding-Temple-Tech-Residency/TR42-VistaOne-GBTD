from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.vendors import Vendor


class VendorService:

    @staticmethod
    async def list(db: AsyncSession):
        result = await db.execute(select(Vendor))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, vendor_id: int):
        result = await db.execute(
            select(Vendor).where(Vendor.id == vendor_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, data: dict):
        vendor = Vendor(**data)
        db.add(vendor)
        await db.commit()
        await db.refresh(vendor)
        return vendor

    @staticmethod
    async def update(db: AsyncSession, vendor: Vendor, updates: dict):
        for key, value in updates.items():
            setattr(vendor, key, value)
        await db.commit()
        await db.refresh(vendor)
        return vendor

    @staticmethod
    async def delete(db: AsyncSession, vendor: Vendor):
        await db.delete(vendor)
        await db.commit()
