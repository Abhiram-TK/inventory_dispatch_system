from pydantic import BaseModel, Field

class TransactionCreatedEvent(BaseModel):

    transaction_id: int 
    invoice_number: str 
    product_id: int 
    quantity: int 

    class Config:

        json_schema_extra = {"example": {"transaction_id": 1001, "invoice_number": "INV-6235", "product_id": 4, "quantity": 14}}