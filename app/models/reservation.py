from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CheckConstraint

from datetime import datetime

from app.database.connection import Base

class Reservation(Base):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)

    batch_id = Column(Integer, ForeignKey("inventory_batches.id"))

    reserved_quantity = Column(Integer, nullable=False)

    status = Column(String, nullable=False)

    reserved_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("reserved_quantity > 0", name="check_reserved_quantity_positive"),
    )

    
    