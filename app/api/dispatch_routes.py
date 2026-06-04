from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

from app.schemas.dispatch_schema import (DispatchCreate, DispatchResponse)

from app.core.logger import logger

router = APIRouter()

@router.get("/dispatch", response_model=list[DispatchResponse])

def get_dispatch(db: Session = Depends(get_db)):

    dispatches = db.query(Dispatch).all()

    return dispatches

@router.post("/dispatch", response_model=DispatchResponse)

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

    return dispatch