from datetime import datetime, timedelta

from app.workers.celery_app import celery_app

from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.reservation import Reservation
from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch

from app.core.logger import logger

@celery_app.task
def expire_reservation():

    logger.info("Reservation cleanup worker started")

    db = SessionLocal()

    try:

        timeout_limit = datetime.utcnow() - timedelta(minutes=1)

        reservations = (db.query(Reservation).filter(Reservation.status == "RESERVED", Reservation.reserved_at < timeout_limit).all())

        logger.info(f"Expired reservations found: {len(reservations)}")

        for reservation in reservations:

            batch = (db.query(InventoryBatch).filter(InventoryBatch.id == reservation.batch_id).first())

            if batch:

                batch.quantity_available += reservation.reserved_quantity

                logger.info(f"Inventory restored | Batch ID: {batch.id} | Quantity Restored: {reservation.reserved_quantity}")

            reservation.status = "EXPIRED"

            logger.info(f"Reservation expired | Reservation ID: {reservation.id}")

        db.commit()

        logger.info("Reservation cleanup completed successfully")

    except Exception as e:
    
        db.rollback()
    
        logger.error(f"Reservation cleanup worker failed: {str(e)}")

        raise

    finally:

        db.close()