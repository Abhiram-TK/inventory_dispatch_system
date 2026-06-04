from sqlalchemy import (Column, Integer, String, ForeignKey, Date, CheckConstraint)

from sqlalchemy.orm import relationship

from app.database.connection import Base

class InventoryBatch(Base):

    __tablename__ = "inventory_batches"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    batch_number = Column(String, unique=True, nullable=False)

    quantity_available = Column(Integer, nullable=False)

    manufacturing_date = Column(Date, nullable=False)

    warranty_months = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="batches")

    reservations = relationship("Reservation", back_populates="batch")

    __table_args__ = (CheckConstraint('quantity_available >= 0', name='check_quantity_non_negative'),)