from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation

from app.core.logger import logger

from sqlalchemy.exc import SQLAlchemyError

def create_product(name, sku, price):
    
    db = SessionLocal()

    existing_product = (db.query(Product).filter(Product.sku == sku).first())

    if existing_product:

        logger.info(f"Product already exists: {sku}")

        return existing_product

    new_product = Product(name=name, sku=sku, price=price)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    logger.info(f"Invenotry created: {new_product.sku}")

    db.close()

    return new_product

def create_inventory_batch(product_id, batch_number, quantity_available, manufacturing_date, warranty_months):

    db = SessionLocal()

    existing_batch = (db.query(InventoryBatch).filter(InventoryBatch.batch_number == batch_number).first())

    if existing_batch:

        logger.info(f"Batch already exists: {batch_number}")

        db.close()

        return existing_batch

    new_batch = InventoryBatch(product_id=product_id, batch_number=batch_number, quantity_available= quantity_available, manufacturing_date=manufacturing_date, 
                               warranty_months=warranty_months)

    db.add(new_batch)
    db.commit()
    db.refresh(new_batch)

    logger.info(f"Inventory batch created: {new_batch.batch_number}")

    db.close()

    return new_batch

def reserve_inventory(batch_id, reserve_quantity):

    db = SessionLocal()

    try:

        batch = db.query(InventoryBatch).filter(InventoryBatch.id == batch_id).with_for_update().first()

        if not batch:

            logger.error(f"Inventory not found: Batch ID {batch_id}")

            raise Exception("Inventory batch not found")
        
        logger.info(
            f"Attempting reservation | "
            f"Batch ID: {batch.id} | "
            f"Available Quantity: {batch.quantity_available} | "
            f"Requested Quantity: {reserve_quantity}"
        )

        if batch.quantity_available < reserve_quantity:

            logger.error(f"Stock exhaustion: Batch {batch.id} has only {batch.quantity_available}, requested {reserve_quantity}")

            raise Exception("Insufficient inventory available")

        batch.quantity_available -= reserve_quantity

        reservation = Reservation(batch_id=batch.id, reserved_quantity=reserve_quantity, status="RESERVED")

        db.add(reservation)
        db.commit()
        db.refresh(reservation)

        logger.info(
            f"Reservation created | "
            f"Reservation ID: {reservation.id} | "
            f"Batch ID: {batch.id} | "
            f"Reserved Quantity: {reserve_quantity} | "
            f"Remaining Quantity: {batch.quantity_available}"
        )

        return reservation

    except SQLAlchemyError as error:

        db.rollback()

        logger.error(f"Database exception: {error}")

        raise

    except Exception as error:

        db.rollback()

        logger.error(f"Reservation failed: {error}")

        raise

    finally:

        db.close()