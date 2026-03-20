from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base


class WorkOrder(Base):
    __tablename__ = "workorders"

    workorder_id = Column(Integer, primary_key=True)
    auth_user_id = Column(UUID(as_uuid=True), ForeignKey("user_profiles.auth_user_id"), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)

    workorder_status = Column(String, nullable=False)
    total_amount = Column(Numeric, nullable=False)
    work_description = Column(String)

    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
