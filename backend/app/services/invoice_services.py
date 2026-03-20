from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.invoices import Invoice


class InvoiceService:

    @staticmethod
    async def list_for_user(db: AsyncSession, user):
        if user.role == "admin":
            result = await db.execute(select(Invoice))
        else:
            result = await db.execute(
                select(Invoice).where(Invoice.auth_user_id == user.id)
            )
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, invoice_id: int):
        result = await db.execute(
            select(Invoice).where(Invoice.invoice_id == invoice_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, user, data: dict):
        data["auth_user_id"] = user.id
        invoice = Invoice(**data)
        db.add(invoice)
        await db.commit()
        await db.refresh(invoice)
        return invoice

    @staticmethod
    async def update(db: AsyncSession, invoice: Invoice, updates: dict):
        for key, value in updates.items():
            setattr(invoice, key, value)
        await db.commit()
        await db.refresh(invoice)
        return invoice

    @staticmethod
    async def delete(db: AsyncSession, invoice: Invoice):
        await db.delete(invoice)
        await db.commit()
