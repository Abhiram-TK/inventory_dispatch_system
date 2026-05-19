from app.models.product import Product

from app.models.inventory_batch import InventoryBatch

from app.models.reservation import Reservation

from app.models.dispatch import Dispatch

product = Product(name="Laptop", sku="LAP999", price=50000)

batch = InventoryBatch(batch_number="BATCH001", quantity_available=10)

reservation = Reservation(reserved_quantity=2, status="RESERVED")

dispatch = Dispatch(vehicle_number="KL07AB1234", status="SHIPPED")

product.batches.append(batch)

batch.reservations.append(reservation)

reservation.dispatch = dispatch

print(product.batches)

print(batch.product)

print(batch.reservations)

print(reservation.batch)

print(reservation.dispatch)

print(dispatch.reservation)