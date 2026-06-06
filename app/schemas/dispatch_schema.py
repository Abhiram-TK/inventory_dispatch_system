from pydantic import BaseModel

class DispatchCreate(BaseModel):

    reservation_id: int 
    vehicle_number: str 

    class Config:

        json_schema_extra = {"example": {"reservation_id": 223, "vehicle_number": "KL07JD8364"}}

class DispatchResponse(BaseModel):

    dispatch_id: int
    reservation_id: int
    vehicle_number: str
    status: str