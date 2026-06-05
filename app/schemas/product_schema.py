from pydantic import BaseModel

class ProductResponse(BaseModel):

    id: int
    name: str
    sku: str
    price: float

    class Config:

        from_attributes = True