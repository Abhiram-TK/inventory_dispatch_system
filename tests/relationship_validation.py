from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation

db = SessionLocal()

print("\n------ PRODUCT --> BATCHES VALIDATION ------")

product = db.query(Product).first()

if not product:

    print("No products found")

    db.close()

    exit()

print(f"\nProduct: {product.name}")

print("\nLinked Inventory Batches:")

print("\nShowing first 10 batches...")

for batch in sorted(product.batches, key=lambda batch: batch.manufacturing_date)[:10]:

    print(f"Batch Number: {batch.batch_number} | "
          f"MFG Date: {batch.manufacturing_date} | "
          f"Quantity: {batch.quantity_available}")
    
print("\n------ BATCH --> RESERVATIONS VALIDATION ------")

batch = db.query(InventoryBatch).filter(InventoryBatch.reservations.any()).first()

print(f"\nBatch: {batch.batch_number}")

print("\nLinked Reservations:")

print(f"\nTotal Reservations: "
      f"{len(batch.reservations)}")

for reservation in sorted(batch.reservations, key=lambda reservation: reservation.id):

    print(f"\nReservation ID: {reservation.id} | "
          f"Reserved Quantity: {reservation.reserved_quantity}")
    
print("\n------ RESERVATION --> DISPATCH VALIDATION ------")

reservation = db.query(Reservation).first()

print(f"\nReservation ID: {reservation.id}")

print("\nDispatch Relationship:")

if reservation.dispatch:

    print(
        f"Dispatch ID: {reservation.dispatch.id} | "
        f"Vehicle Number: {reservation.dispatch.vehicle_number} | "
        f"Status: {reservation.dispatch.status}"
    )

else:

    print("No dispatch found")

db.close()