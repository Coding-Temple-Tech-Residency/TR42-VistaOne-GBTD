from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UserProfileBase(BaseModel):
    role: str


class UserProfileCreate(UserProfileBase):
    auth_user_id: UUID


class UserProfileResponse(UserProfileBase):
    id: UUID
    auth_user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
