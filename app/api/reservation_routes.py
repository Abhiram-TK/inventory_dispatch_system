from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.reservation import Reservation

from app.schemas.reservation_schema import ReservationListResponse

from typing import Optional

router = APIRouter(tags=["Reservations"])

@router.get("/reservations", response_model=list[ReservationListResponse], summary="View Reservations", description="""
            Retrieve reservation records.

            Supports:

            - Viewing all reservations
            - Filtering by Reservation ID
            - Tracking reservation status

            Possible statuses:

            - RESERVED
            - DISPATCHED
            - EXPIRED

            Used to monitor inventory allocation lifecycle.
            """)

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