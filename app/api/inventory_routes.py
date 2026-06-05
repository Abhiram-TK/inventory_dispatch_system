from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.inventory_batch import InventoryBatch

from app.schemas.inventory_schema import InventoryResponse
from app.schemas.reservation_schema import ReservationRequest, ReservationResponse

from app.operations.inventory_ops import reserve_inventory

from typing import Optional

router = APIRouter()

@router.get("/inventory", response_model=list[InventoryResponse])

def get_inventory(product_id: Optional[int] = Query(None, gt=0, description="Product ID"), db: Session = Depends(get_db)):

    query = db.query(InventoryBatch)

    if product_id:

        query = query.filter(InventoryBatch.product_id == product_id)

    inventory = query.order_by(InventoryBatch.id).all()

    response = []

    for batch in inventory:

        response.append({"batch_id": batch.id, "product_id": batch.product_id, "product_name": batch.product.name, "batch_number": batch.batch_number,
                         "quantity_available": batch.quantity_available, "manufacturing_date": batch.manufacturing_date, "warranty_months": batch.warranty_months})

    return response

@router.post("/inventory/reserve", response_model=ReservationResponse)

def create_reservation(reservation_data: ReservationRequest):

    try:

        reservation = reserve_inventory(batch_id=reservation_data.batch_id, reserve_quantity=reservation_data.quantity)

        return {"reservation_id": reservation.id, "status": reservation.status}

    except Exception as error:

        raise HTTPException(status_code=400, detail=str(error))