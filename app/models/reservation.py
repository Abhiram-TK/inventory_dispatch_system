from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CheckConstraint

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.connection import Base

class Reservation(Base):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)

    transaction_id = Column(Integer, nullable=True, index=True)

    batch_id = Column(Integer, ForeignKey("inventory_batches.id"))

    reserved_quantity = Column(Integer, nullable=False)

    status = Column(String, nullable=False)

    reserved_at = Column(DateTime, default=datetime.utcnow)

    batch = relationship("InventoryBatch", back_populates="reservations")

    dispatch = relationship("Dispatch", back_populates="reservation", uselist=False)

    __table_args__ = (CheckConstraint("reserved_quantity > 0", name="check_reserved_quantity_positive"),)