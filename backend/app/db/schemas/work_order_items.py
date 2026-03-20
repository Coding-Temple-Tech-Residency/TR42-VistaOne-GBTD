from pydantic import BaseModel
from datetime import datetime


class WorkOrderItemBase(BaseModel):
    description: str
    quantity: int
    unit_price: float
    subtotal: float


class WorkOrderItemCreate(WorkOrderItemBase):
    pass


class WorkOrderItemUpdate(BaseModel):
    description: str | None = None
    quantity: int | None = None
    unit_price: float | None = None
    subtotal: float | None = None


class WorkOrderItemResponse(WorkOrderItemBase):
    workorder_item_id: int
    workorder_id: int
    created_at: datetime

    class Config:
        orm_mode = True
