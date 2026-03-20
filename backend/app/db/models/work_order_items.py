from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base


class WorkOrderItem(Base):
    __tablename__ = "workorder_items"

    workorder_item_id = Column(Integer, primary_key=True)
    workorder_id = Column(Integer, ForeignKey("workorders.workorder_id"), nullable=False)

    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric, nullable=False)
    subtotal = Column(Numeric, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
