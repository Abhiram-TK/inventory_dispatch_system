from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch
from app.models.reservation import Reservation

from app.database.connection import SessionLocal

from app.operations.inventory_ops import reserve_inventory

from app.core.logger import logger

logger.info("Inventory system started")

print("\nTesting transactional reservation workflow...")

db = SessionLocal()

product = db.query(Product).first()

if not product:

    raise Exception("No products found. Run seed_data.py first.")

batch = (db.query(InventoryBatch).filter(InventoryBatch.product_id == product.id).first())

if not batch:

    raise Exception("No inventory batches found. Run seed_data.py first.")

print(f"Product ID: {product.id}")
print(f"Batch ID: {batch.id}")
print(f"Available Quantity: {batch.quantity_available}")

print("\nSUCCESS CASE")

reservation = reserve_inventory(batch_id=batch.id, reserve_quantity=4)

db.close()

db = SessionLocal()

updated_batch = (db.query(InventoryBatch).filter(InventoryBatch.id == batch.id).first())

if reservation:
    print("Reservation successful")
    print(f"Reserved Quantity: {reservation.reserved_quantity}")
    print(f"Available Quantity After Reservation: {updated_batch.quantity_available}")

print("\nFAILURE CASE - REQUESTING 50000 UNITS")

try:

     reserve_inventory(batch_id=batch.id,reserve_quantity=50000)

except Exception as e:

    print("Over-reservation blocked safely")

db.close()

