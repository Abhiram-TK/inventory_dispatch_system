from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.permission_checker import PermissionChecker

from app.models.reservation import Reservation

from app.schemas.reservation_schema import ReservationListResponse
from app.schemas.reservation_schema import ReservationStatusResponse

from typing import Optional

router = APIRouter(tags=["Reservations"])

@router.get("/reservations", response_model=list[ReservationListResponse], summary="View Reservations", dependencies=[Depends(PermissionChecker(["view_reservations"]))], description="""
           Retrieve inventory reservations.

            Requires:

            - view_reservations permission

            Returns reservation records with current status.""")

def get_reservations(reservation_id: Optional[int] = None,db: Session = Depends(get_db)):

    query = db.query(Reservation)

    if reservation_id:

        query = query.filter(Reservation.id == reservation_id)

    reservations = query.all()

    response = []

    for reservation in reservations:

        response.append(
            {"reservation_id": reservation.id, "batch_id": reservation.batch_id, "reserved_quantity": reservation.reserved_quantity, "status": reservation.status,
             "reserved_at": reservation.reserved_at})

    return response

@router.get("/reservations/transaction/{transaction_id}", response_model=ReservationStatusResponse, summary="Get Reservation By Transaction ID", dependencies=[Depends(PermissionChecker(["view_reservations"]))], description=
            """Retrieve reservation status using transaction ID.

            Used by Project 1 to correlate transactions and inventory reservations.""")

def get_reservation_by_transaction(transaction_id: int, db: Session = Depends(get_db)):

    reservation = (db.query(Reservation).filter(Reservation.transaction_id == transaction_id).first())

    if not reservation:

        raise HTTPException(status_code=404, detail="Reservation not found")

    return {"transaction_id": transaction_id, "reservation_id": reservation.id, "status": reservation.status}