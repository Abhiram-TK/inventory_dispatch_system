from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

from datetime import date

from app.operations.inventory_ops import (create_product, create_inventory_batch,reserve_inventory)

from app.core.logger import logger

logger.info("Inventory system started")

print("Testing transactional reservation workflow...")

product = create_product(name="Mousepad", sku="PAD004", price=750)

print(product.id)

batch = create_inventory_batch(product_id=product.id, batch_number="BATCH-PAD-003", quantity_available=10, expiry_date=date(2027, 12, 31))

print(batch.quantity_available)

print("\nSUCCESS CASE")

reservation = reserve_inventory(batch_id=batch.id, reserve_quantity=4)

if reservation:
    print("Reservation successful")
    print(reservation.reserved_quantity)

print("\nFAILURE CASE")

try:

    failed_reservation = reserve_inventory(batch_id=batch.id, reserve_quantity=50)

except Exception as e:

    print(f"Over-reservation blocked safely: {e}")