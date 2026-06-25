from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

from app.schemas.dispatch_schema import (DispatchCreate, DispatchResponse)

from app.core.logger import logger

from app.services.permission_checker import PermissionChecker

from typing import Optional

router = APIRouter(tags=["Dispatch"])

@router.post("/dispatch", response_model=DispatchResponse, summary="Create Dispatch", dependencies=[Depends(PermissionChecker(["dispatch_inventory"]))], description="""
            Dispatch reserved inventory.

            Requires:

            - dispatch_inventory permission

            Returns dispatch details for the reservation.""")

def create_dispatch(dispatch_data: DispatchCreate, db: Session = Depends(get_db)):

    reservation = (db.query(Reservation).filter(Reservation.id == dispatch_data.reservation_id).first())

    if not reservation:

        raise HTTPException(status_code=404, detail="Reservation not found")

    if reservation.status != "RESERVED":

        raise HTTPException(status_code=400, detail="Only RESERVED inventory can be dispatched")

    dispatch = Dispatch(reservation_id=dispatch_data.reservation_id, vehicle_number=dispatch_data.vehicle_number, status="DISPATCHED")

    db.add(dispatch)

    reservation.status = "DISPATCHED"

    db.commit()

    db.refresh(dispatch)

    logger.info(
    f"Dispatch created | "
    f"Dispatch ID: {dispatch.id} | "
    f"Reservation ID: {reservation.id} | "
    f"Vehicle: {dispatch.vehicle_number}")

    return {"dispatch_id": dispatch.id, "reservation_id": dispatch.reservation_id, "vehicle_number": dispatch.vehicle_number, "status": dispatch.status}

@router.get("/dispatch", response_model=list[DispatchResponse], summary="View Dispatches", dependencies=[Depends(PermissionChecker(["view_dispatches"]))], description="""
            Retrieve dispatch records.

            Requires:

            - view_dispatches permission

            Returns completed and pending dispatches.""")

def get_dispatch(reservation_id: Optional[int] = None,db: Session = Depends(get_db)):

    query = db.query(Dispatch)

    if reservation_id:

        query = query.filter(Dispatch.reservation_id == reservation_id)

    dispatches = query.all()

    response = []

    for dispatch in dispatches:

        response.append({"dispatch_id": dispatch.id, "reservation_id": dispatch.reservation_id, "vehicle_number": dispatch.vehicle_number, "status": dispatch.status})

    return response