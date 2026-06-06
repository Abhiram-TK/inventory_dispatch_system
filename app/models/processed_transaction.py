from sqlalchemy import Column, Integer, String, DateTime

from datetime import datetime

from app.database.connection import Base

class ProcessedTransaction(Base):

    __tablename__ = "processed_transactions"

    id = Column(Integer, primary_key=True)

    transaction_id = Column(Integer, unique=True, nullable=False)

    invoice_number = Column(String, nullable=False)

    processed_at = Column(DateTime, default=datetime.utcnow)