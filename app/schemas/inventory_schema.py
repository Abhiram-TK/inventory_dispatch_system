from pydantic import BaseModel

class InventoryResponse(BaseModel):

    id: int
    product_id: int
    batch_number: str
    quantity_available: int
    manufacturing_date: str
    warranty_months: int

    class Config:

        from_attributes = True