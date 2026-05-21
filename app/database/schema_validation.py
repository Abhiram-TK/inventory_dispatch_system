from app.database.seed_data import (seed_fake_product, seed_inventory_batches, seed_fake_reservations)

from app.database.connection import SessionLocal

from app.models.inventory_batch import InventoryBatch

print("\n------ STARTING SCHEMA STABILITY VALIDATION ------")

for cycle in range(3):

    print(f"\nRunning Validation Cycle: {cycle + 1}")

    seed_fake_product(count=10)

    seed_inventory_batches()

    seed_fake_reservations(count=20)

print("\nRepeated operations completed.")

db = SessionLocal()

negative_inventory = db.query(InventoryBatch).filter(InventoryBatch.quantity_available < 0).all()

if negative_inventory:

    print("\nSCHEMA VALIDATION FAILED!")
    print("Negative inventory detected!")

else:

    print("\nSchema Stability Validation PASSED!")
    print("No negative inventory found.")

db.close()

