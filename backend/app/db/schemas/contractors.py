from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class ContractorBase(BaseModel):
    name: str
    assignment: Optional[str] = None
    invoice_id: Optional[int] = None


class ContractorCreate(ContractorBase):
    pass


class ContractorUpdate(BaseModel):
    name: Optional[str] = None
    assignment: Optional[str] = None


class ContractorResponse(ContractorBase):
    category_id: int
    auth_user_id: Optional[UUID]
    created_at: datetime

    class Config:
        orm_mode = True
