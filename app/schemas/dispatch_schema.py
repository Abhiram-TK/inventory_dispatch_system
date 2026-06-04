from pydantic import BaseModel

class DispatchRequest(BaseModel):

    reservation_id: int
    vehicle_number: str

class DispatchResponse(BaseModel):

    dispatch_id: int
    status: str