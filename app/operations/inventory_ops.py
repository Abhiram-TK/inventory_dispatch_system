from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation

def create_product(name, sku, price):
    
    db = SessionLocal()

    new_product = Product(name=name, sku=sku, price=price)

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    db.close()

    return new_product

def create_inventory_batch(product_id, batch_number, quantity_available, expiry_date):

    db = SessionLocal()

    new_batch = InventoryBatch(product_id=product_id, batch_number=batch_number, quantity_available= quantity_available, expiry_date=expiry_date)

    db.add(new_batch)

    db.commit()

    db.refresh(new_batch)

    db.close()

    return new_batch

def reserve_inventory(batch_id, reserved_quantity, status):

    db = SessionLocal()

    new_reservation = Reservation(batch_id=batch_id, reserved_quantity=reserved_quantity, status=status)

    db.add(new_reservation)

    batch = db.query(InventoryBatch).filter(InventoryBatch.id == batch_id).first()

    batch.quantity_available -= reserved_quantity

    db.commit()

    db.refresh(new_reservation)

    db.close()

    return new_reservation