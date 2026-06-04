from pydantic import BaseModel

class InventoryResponse(BaseModel):

    id: int
    batch_number: str
    quantity_available: int