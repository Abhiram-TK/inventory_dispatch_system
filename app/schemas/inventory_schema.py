from pydantic import BaseModel

from datetime import date

class InventoryResponse(BaseModel):

    batch_id: int
    product_id: int
    product_name: str
    batch_number: str
    quantity_available: int
    manufacturing_date: date
    warranty_months: int

    class Config:

        from_attributes = True