from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

from datetime import date

from app.operations.inventory_ops import (create_product, create_inventory_batch, reserve_inventory)

print("Tesing CRUD operations...")

product = create_product(name="Laptop", sku="LAPTOP003", price=50000)

print(product.id)
print(product.name)

batch = create_inventory_batch(product_id=product.id, batch_number="BATCH003", quantity_available=50, expiry_date=date(2027, 12, 31))

print(batch.id)
print(batch.quantity_available)

reservation = reserve_inventory(batch_id=batch.id, reserved_quantity=5, status="RESERVED")

print(reservation.id)
print(reservation.status)

print("CRUD operations completed successfully!")

