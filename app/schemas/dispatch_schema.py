from pydantic import BaseModel

class DispatchCreate(BaseModel):

    reservation_id: int
    vehicle_number: str

class DispatchResponse(BaseModel):

    id: int
    reservation_id: int
    vehicle_number: str
    status: str

    class Config:

        from_attributes = True