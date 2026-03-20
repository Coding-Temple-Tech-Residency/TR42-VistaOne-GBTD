from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.work_order_items import WorkOrderItem


class WorkOrderItemService:

    @staticmethod
    async def list_for_workorder(db: AsyncSession, workorder_id: int):
        result = await db.execute(
            select(WorkOrderItem).where(WorkOrderItem.workorder_id == workorder_id)
        )
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, item_id: int):
        result = await db.execute(
            select(WorkOrderItem).where(WorkOrderItem.workorder_item_id == item_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, workorder_id: int, data: dict):
        data["workorder_id"] = workorder_id
        item = WorkOrderItem(**data)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def update(db: AsyncSession, item: WorkOrderItem, updates: dict):
        for key, value in updates.items():
            setattr(item, key, value)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, item: WorkOrderItem):
        await db.delete(item)
        await db.commit()
