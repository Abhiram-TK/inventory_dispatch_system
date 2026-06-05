from pydantic import BaseModel

from datetime import datetime

class ReservationRequest(BaseModel):

    batch_id: int
    quantity: int

class ReservationResponse(BaseModel):

    reservation_id: int
    status: str

class ReservationListResponse(BaseModel):

    reservation_id: int
    batch_id: int
    reserved_quantity: int
    status: str
    reserved_at: datetime

    class Config:

        from_attributes = True