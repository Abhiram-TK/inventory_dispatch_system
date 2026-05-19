from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.connection import Base

class Dispatch(Base):

    __tablename__ = "dispatches"

    id = Column(Integer, primary_key=True)

    reservation_id = Column(Integer, ForeignKey("reservations.id"))

    dispatch_date = Column(DateTime, default=datetime.utcnow)

    vehicle_number = Column(String, nullable=False)

    status = Column(String, nullable=False)

    reservation = relationship("Reservation", back_populates="dispatch")

