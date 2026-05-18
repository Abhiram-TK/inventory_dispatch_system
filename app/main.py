from datetime import date

from app.models.inventory_batch import InventoryBatch

sample_batch = InventoryBatch(
    product_id=1,
    batch_number="LAPTOPBATCH001",
    quantity_available=500,
    expiry_date=date(2027, 1, 1)
)

print(sample_batch.batch_number)
print(sample_batch.quantity_available)
print(sample_batch.expiry_date)

