from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

from datetime import date

from app.operations.inventory_ops import (
    create_product,
    create_inventory_batch,
    reserve_inventory
)

print("Testing transactional reservation workflow...")

# CREATE PRODUCT
product = create_product(
    name="Mousepad",
    sku="PAD003",
    price=750
)

print(product.id)

# CREATE INVENTORY BATCH
batch = create_inventory_batch(
    product_id=product.id,
    batch_number="BATCH-PAD-002",
    quantity_available=10,
    expiry_date=date(2027, 12, 31)
)

print(batch.quantity_available)

# SUCCESS CASE
print("\nSUCCESS CASE")

reservation = reserve_inventory(
    batch_id=batch.id,
    reserve_quantity=4
)

if reservation:
    print("Reservation successful")
    print(reservation.reserved_quantity)

# FAILURE CASE
print("\nFAILURE CASE")

failed_reservation = reserve_inventory(
    batch_id=batch.id,
    reserve_quantity=50
)

if failed_reservation is None:
    print("Over-reservation blocked safely")