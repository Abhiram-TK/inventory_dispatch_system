from app.database.connection import Base, engine

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch
from app.models.processed_transaction import ProcessedTransaction

Base.metadata.create_all(bind=engine)

print("Tables created successfully")