from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation

from app.core.logger import logger

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

    db.close()

    return new_product

def create_inventory_batch(product_id, batch_number, quantity_available, expiry_date):

    db = SessionLocal()

    existing_batch = (db.query(InventoryBatch).filter(InventoryBatch.batch_number == batch_number).first())

    if existing_batch:

        logger.info(f"Batch already exists: {batch_number}")

        db.close()

        return existing_batch

    new_batch = InventoryBatch(product_id=product_id, batch_number=batch_number, quantity_available= quantity_available, expiry_date=expiry_date)

    db.add(new_batch)


    db.commit()

    db.refresh(new_batch)

    db.close()

    return new_batch

def reserve_inventory(batch_id, reserve_quantity):

    db = SessionLocal()

    try:

        batch = db.query(InventoryBatch).filter(
            InventoryBatch.id == batch_id
        ).first()

        # Validate requested inventory availability before reservation

        if not batch:
            raise Exception("Inventory batch not found")

        if batch.quantity_available < reserve_quantity:
            raise Exception("Insufficient inventory available")

        # Reduce available inventory as part of transactional reservation workflow

        batch.quantity_available -= reserve_quantity

        # Create reservation record after successful inventory validation

        reservation = Reservation(
            batch_id=batch.id,
            reserved_quantity=reserve_quantity,
            status="RESERVED"
        )

        db.add(reservation)

        db.commit()

        db.refresh(reservation)

        return reservation

    except Exception as error:

        # Rollback transaction to preserve inventory consistency on failure

        db.rollback()

        print(f"Transaction failed: {error}")

        raise

    finally:

        db.close()