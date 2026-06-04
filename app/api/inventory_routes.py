from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.inventory_batch import InventoryBatch

from app.schemas.inventory_schema import InventoryResponse
from app.schemas.reservation_schema import ReservationRequest, ReservationResponse

from app.operations.inventory_ops import reserve_inventory

router = APIRouter()

@router.get("/inventory", response_model=list[InventoryResponse])

def get_inventory(db: Session = Depends(get_db)):

    inventory = db.query(InventoryBatch).all()

    return inventory

@router.post("/inventory/reserve", response_model=ReservationResponse)

def create_reservation(reservation_data: ReservationRequest):

    reservation = reserve_inventory(batch_id=reservation_data.batch_id, reserve_quantity=reservation_data.quantity)

    return {"reservation_id": reservation.id, "status": reservation.status}