from sqlalchemy import Column, Integer, String, Numeric, Date, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True)
    workorder_id = Column(Integer, ForeignKey("workorders.workorder_id"), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    auth_user_id = Column(UUID(as_uuid=True), ForeignKey("user_profiles.auth_user_id"), nullable=False)

    invoice_number = Column(String, unique=True, nullable=False)
    invoice_status = Column(String, nullable=False)

    subtotal = Column(Numeric, nullable=False)
    tax_amount = Column(Numeric, default=0)
    discount_amount = Column(Numeric, default=0)
    total_amount = Column(Numeric, nullable=False)

    due_date = Column(Date)
    paid_date = Column(Date)
    payment_method = Column(String)

    billing_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)

    notes = Column(Text)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
