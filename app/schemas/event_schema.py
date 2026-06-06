from pydantic import BaseModel

class TransactionCreatedEvent(BaseModel):

    transaction_id: int
    invoice_number: str
    product_id: int
    quantity: int

    class Config:

        json_schema_extra = {"example": {"transaction_id": 1001, "invoice_number": "INV-1001", "product_id": 1, "quantity": 5}}