from fastapi import APIRouter

from app.schemas.event_schema import TransactionCreatedEvent

from app.events.reservation_event_handler import (process_transaction_created)

router = APIRouter(tags=["Events"])

@router.post("/events/transaction-created", summary="Simulate Transaction Event", description="""
             Simulate an incoming transaction event.

             This endpoint temporarily replaces Project 1 integration.

             Workflow:

             Transaction Event
             → Inventory Selection
             → Reservation Creation

             Used for testing event-driven inventory allocation before Project 1 integration.
             """)

def create_transaction_event(event: TransactionCreatedEvent):

    result = process_transaction_created(event.model_dump())

    return result