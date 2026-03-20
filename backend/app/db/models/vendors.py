from sqlalchemy import Column, BigInteger, TIMESTAMP, JSON, String
from sqlalchemy.sql import func
from app.db import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(BigInteger, primary_key=True)
    inserted_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    data = Column(JSON)
    name = Column(String)
