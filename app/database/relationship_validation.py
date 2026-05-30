from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation

db = SessionLocal()

print("\n------ PRODUCT --> BATCHES VALIDATION ------")

product = db.query(Product).first()

print(f"\nProduct: {product.name}")

print("\nLinked Inventory Batches:")

for batch in product.batches:

    print(f"Batch Number: {batch.batch_number} | "
          f"Quantity: {batch.quantity_available}")
    
print("\n------ BATCH --> RESERVATIONS VALIDATION ------")

batch = db.query(InventoryBatch).filter(InventoryBatch.reservations.any()).first()

print(f"\nBatch: {batch.batch_number}")

print("\nLinked Reservations:")

for reservation in batch.reservations:

    print(f"Reservation ID: {reservation.id} | "
          f"Reserved Quantity: {reservation.reserved_quantity}")
    
print("\n------ RESERVATION --> DISPATCH VALIDATION ------")

reservation = db.query(Reservation).first()

print(f"\nResevation ID: {reservation.id}")

print("\nDispatch Relationship:")

print(reservation.dispatch)

db.close()