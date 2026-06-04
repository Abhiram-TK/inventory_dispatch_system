from pydantic import BaseModel

class ReservationRequest(BaseModel):

    batch_id: int
    quantity: int

class ReservationResponse(BaseModel):

    reservation_id: int
    status: str