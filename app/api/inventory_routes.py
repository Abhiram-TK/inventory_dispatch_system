from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.inventory_batch import InventoryBatch

from app.schemas.inventory_schema import InventoryResponse
from app.schemas.reservation_schema import ReservationRequest, ReservationResponse

from app.operations.inventory_ops import reserve_inventory

from app.services.rbac_service import RoleChecker

from typing import Optional

router = APIRouter(tags=["Inventory"])

@router.get("/inventory", response_model=list[InventoryResponse], summary="View Inventory Batches", dependencies=[Depends(RoleChecker(["viewer", "recruiter", 
            "support", "auditor", "manager", "admin"]))],description="""
            Retrieve inventory batches currently available in stock.

            Features:

            - Optional filtering by Product ID
            - FIFO visibility using manufacturing dates
            - Available quantity tracking
            - Batch-level inventory inspection

            Used before creating reservations.
            """)

def get_inventory(product_id: Optional[int] = Query(None, gt=0, description="Product ID"), db: Session = Depends(get_db)):

    query = db.query(InventoryBatch)

    if product_id:

        query = query.filter(InventoryBatch.product_id == product_id)

    inventory = query.order_by(InventoryBatch.manufacturing_date).all()

    response = []

    for batch in inventory:

        response.append({"batch_id": batch.id, "product_id": batch.product_id, "product_name": batch.product.name, "batch_number": batch.batch_number,
                         "quantity_available": batch.quantity_available, "manufacturing_date": batch.manufacturing_date, "warranty_months": batch.warranty_months})

    return response

@router.post("/inventory/reserve", response_model=ReservationResponse, summary="Reserve Inventory", dependencies=[Depends(RoleChecker(["recruiter", "manager", "admin"]))], 
             description="""
             Reserve inventory from a specific batch.

             This operation:

             - Validates inventory availability
             - Applies row-level locking
             - Creates a reservation record
             - Reduces available inventory

             Used before dispatch creation.
            """)

def create_reservation(reservation_data: ReservationRequest):

    try:

        reservation = reserve_inventory(batch_id=reservation_data.batch_id, reserve_quantity=reservation_data.quantity)

        return {"reservation_id": reservation.id, "status": reservation.status}

    except Exception as error:

        raise HTTPException(status_code=400, detail=str(error))