from faker import Faker

from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

fake = Faker()

db = SessionLocal()

def seed_fake_product(count=50):

    for _ in range(count):

        fake_product = Product(name=fake.word(), sku=f"SKU-{fake.unique.random_int(min=1000, max=999999)}", price=fake.random_int(min=100, max=100000))

        db.add(fake_product)

    db.commit()

    print(f"{count} fake products inserted successfully.")

seed_fake_product()


        


