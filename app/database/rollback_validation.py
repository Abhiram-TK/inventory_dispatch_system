from app.database.connection import SessionLocal

from app.models.inventory_batch import InventoryBatch

from app.operations.inventory_ops import reserve_inventory

db = SessionLocal()

small_batch = db.query(InventoryBatch)\
    .filter(InventoryBatch.quantity_available <=5)\
    .first()

if not small_batch:

    print("No low-quantity batch found.")

    db.close()

    exit()

print("\n------ BEFORE FAILED RESERVATION ------")

print(f"\nBatch: {small_batch.batch_number} | "
      f"Available Quantity: {small_batch.quantity_available}")

try:

    reserve_inventory(batch_id=small_batch.id, reserve_quantity=50)

except Exception as e:

    print("\nReserved Failed Successfully!")

    print(f"Error: {e}")

db.refresh(small_batch)

print("\n------ AFTER FAILED RESERVATION ------")

print(f"Batch: {small_batch.batch_number} | "
      f"Available Quantity: {small_batch.quantity_available}")

if small_batch.quantity_available < 0:

    print("\nROLLBACK FAILED")

else:

    print("\nRollback Validation PASSED!")

db.close()




