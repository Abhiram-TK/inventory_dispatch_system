from datetime import datetime, timedelta

from app.workers.celery_app import celery_app

from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.reservation import Reservation
from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch

@celery_app.task
def expire_reservation():

    db = SessionLocal()

    timeout_limit = datetime.utcnow() - timedelta(minutes=1)

    reservations = (db.query(Reservation).filter(Reservation.status == "RESERVED", Reservation.reserved_at < timeout_limit).all())

    for reservation in reservations:

        batch = (db.query(InventoryBatch).filter(InventoryBatch.id == reservation.batch_id).first())

        if batch:

            batch.quantity_available += reservation.reserved_quantity

        reservation.status = "EXPIRED"

    db.commit()
    db.close()

    return "Reservation cleanup completed"