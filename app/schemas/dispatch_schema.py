from pydantic import BaseModel

class DispatchCreate(BaseModel):

    reservation_id: int
    vehicle_number: str

class DispatchResponse(BaseModel):

    dispatch_id: int
    reservation_id: int
    vehicle_number: str
    status: str