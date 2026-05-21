from faker import Faker

from app.database.connection import SessionLocal

from app.operations.inventory_ops import reserve_inventory

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

import random

PRODUCT_NAMES = ["Gaming Laptop", "Wireless Mouse", "Mechanical Keyboard", "USB-C Hub", "4K Monitor", "External SSD", "Bluetooth Speaker", "Office Chair", "Webcam", 
                 "Ethernet Cable", "Power Bank", "Graphics Card", "Router", "Printer", "Smartphone", "Tablet", "Docking Station", "Microphone", "Projector", "Server Rack"]

fake = Faker()

def seed_fake_product(count=50):

    db = SessionLocal()

    for _ in range(count):

        fake_product = Product(name=random.choice(PRODUCT_NAMES), sku=f"SKU-{fake.unique.random_int(min=1000, max=999999)}", price=fake.random_int(min=100, max=100000))

        db.add(fake_product)

    db.commit()

    print(f"{count} fake products inserted successfully.")

    db.close()

def seed_inventory_batches(count=300):

    db = SessionLocal()

    products = db.query(Product).all()

    for _ in range(count):

        selected_product = random.choice(products)

        batch = InventoryBatch(product_id=selected_product.id, batch_number=f"BATCH-{fake.uuid4()[:8]}",
                                quantity_available=random.randint(10, 500), expiry_date=fake.future_date())
        
        db.add(batch)
    
    db.commit()

    print(f"{count} fake inventory batches inserted successfully!")

    db.close()

def seed_fake_reservations(count=200):

    db = SessionLocal()

    batches = db.query(InventoryBatch).all()

    successful_reservations = 0

    for _ in range(count):

        selected_batch = random.choice(batches)

        reserve_quantity = random.randint(1, 20)

        try:

            reservation = reserve_inventory(batch_id=selected_batch.id, reserve_quantity=reserve_quantity)

            if reservation:
                successful_reservations += 1

        except Exception as e:

            print(f"Reservation failed: {e}")

    print(f"{successful_reservations} reservations created successfully!")

    db.close()

if __name__ == "__main__":

    seed_fake_product()
    seed_inventory_batches()
    seed_fake_reservations()








        


