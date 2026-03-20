from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base


class Contractor(Base):
    __tablename__ = "contractors"

    category_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    assignment = Column(Text)
    invoice_id = Column(Integer)
    auth_user_id = Column(UUID(as_uuid=True), ForeignKey("user_profiles.auth_user_id"))

    created_at = Column(TIMESTAMP, server_default=func.now())
