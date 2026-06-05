from sqlalchemy import Column, Integer, String, Numeric, DateTime, CheckConstraint

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.connection import Base


class Product(Base):

    __tablename__="products"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    sku = Column(String, unique=True, nullable=False)

    price = Column(Numeric, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    batches = relationship("InventoryBatch", back_populates="product")

    __table_args__ = (
        CheckConstraint('price > 0', name='check_price_positive'),)
    
    