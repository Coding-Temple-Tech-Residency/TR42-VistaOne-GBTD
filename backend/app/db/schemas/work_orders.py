from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class WorkOrderBase(BaseModel):
    vendor_id: int
    workorder_status: str
    total_amount: float
    work_description: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None


class WorkOrderCreate(WorkOrderBase):
    pass


class WorkOrderUpdate(BaseModel):
    workorder_status: Optional[str] = None
    total_amount: Optional[float] = None
    work_description: Optional[str] = None


class WorkOrderResponse(WorkOrderBase):
    workorder_id: int
    auth_user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
