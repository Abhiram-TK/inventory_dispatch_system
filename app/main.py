from app.database.connection import Base, engine

from app.models.product import Product

from app.models.inventory_batch import InventoryBatch

from app.models.reservation import Reservation

from app.models.dispatch import Dispatch

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")



