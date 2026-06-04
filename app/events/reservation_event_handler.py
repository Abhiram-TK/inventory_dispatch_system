from app.database.connection import SessionLocal

from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch
from app.models.reservation import Reservation
from app.models.product import Product

from app.operations.inventory_ops import reserve_inventory

from app.core.logger import logger

def process_transaction_created(payload):

    logger.info("\nTRANSACTION_CREATED event received")

    logger.info(f"\nPayload: {payload}")

    transaction_id = payload["transaction_id"]

    invoice_number = payload["invoice_number"]

    product_id = payload["product_id"]

    quantity = payload["quantity"]

    db = SessionLocal()

    batch = db.query(InventoryBatch).filter(InventoryBatch.product_id == product_id).first()

    if not batch:

        logger.error(f"No inventory batch found for product_id={product_id}")

        db.close()

        return
    
    logger.info("Processing reservation")

    logger.info(f"Attempting reservation for Product ID: {product_id}")

    logger.info(f"Requested Quantity: {quantity}")

    try:

        reservation = reserve_inventory(batch_id=batch.id, reserve_quantity=quantity)

        logger.info("Inventory reserved successfully!")

        logger.info(f"Reservation ID: {reservation.id}")

        logger.info(f"Reserved Quantity: {reservation.reserved_quantity}")

    except Exception as e:

        logger.error("Inventory reservation failed.")

        logger.error(f"Reason: {str(e)}")
        
        logger.error("Possible causes:")

        logger.error("- insufficient inventory")

        logger.error("- invalid inventory batch")

        logger.error("- reservation rollback triggered")

    logger.info("Event processing completed.")

    db.close()

