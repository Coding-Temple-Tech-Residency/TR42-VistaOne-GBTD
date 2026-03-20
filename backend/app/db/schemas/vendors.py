from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any


class VendorBase(BaseModel):
    name: Optional[str] = None
    data: Optional[Any] = None


class VendorCreate(VendorBase):
    pass


class VendorUpdate(VendorBase):
    pass


class VendorResponse(VendorBase):
    id: int
    inserted_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
