from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional


class InvoiceBase(BaseModel):
    workorder_id: int
    vendor_id: int
    invoice_number: str
    invoice_status: str
    subtotal: float
    tax_amount: Optional[float] = 0
    discount_amount: Optional[float] = 0
    total_amount: float
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    payment_method: Optional[str] = None
    billing_address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None
    notes: Optional[str] = None


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(BaseModel):
    invoice_status: Optional[str] = None
    notes: Optional[str] = None


class InvoiceResponse(InvoiceBase):
    invoice_id: int
    auth_user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
