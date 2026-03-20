from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.workorders import WorkOrder


class WorkOrderService:

    @staticmethod
    async def list_for_user(db: AsyncSession, user):
        if user.role == "admin":
            result = await db.execute(select(WorkOrder))
        else:
            result = await db.execute(
                select(WorkOrder).where(WorkOrder.auth_user_id == user.id)
            )
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, workorder_id: int):
        result = await db.execute(
            select(WorkOrder).where(WorkOrder.workorder_id == workorder_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, user, data: dict):
        data["auth_user_id"] = user.id
        workorder = WorkOrder(**data)
        db.add(workorder)
        await db.commit()
        await db.refresh(workorder)
        return workorder

    @staticmethod
    async def update(db: AsyncSession, workorder: WorkOrder, updates: dict):
        for key, value in updates.items():
            setattr(workorder, key, value)
        await db.commit()
        await db.refresh(workorder)
        return workorder

    @staticmethod
    async def delete(db: AsyncSession, workorder: WorkOrder):
        await db.delete(workorder)
        await db.commit()
