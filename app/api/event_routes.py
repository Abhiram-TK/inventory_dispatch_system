from fastapi import APIRouter

from app.schemas.event_schema import TransactionCreatedEvent

from app.events.reservation_event_handler import (process_transaction_created)

router = APIRouter()

@router.post("/events/transaction-created")

def create_transaction_event(event: TransactionCreatedEvent):

    result = process_transaction_created(event.model_dump())

    return result