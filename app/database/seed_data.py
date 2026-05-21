from faker import Faker

from app.database.connection import SessionLocal

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.reservation import Reservation
from app.models.dispatch import Dispatch

import random

PRODUCT_NAMES = ["Gaming Laptop", "Wireless Mouse", "Mechanical Keyboard", "USB-C Hub", "4K Monitor", "External SSD", "Bluetooth Speaker", "Office Chair", "Webcam", 
                 "Ethernal Cable", "Power Bank", "Graphics Card", "Router", "Printer", "Smartphone", "Tablet", "Docking Station", "Microphone", "Projector", "Server Rack"]

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

        batch = InventoryBatch(product_id=selected_product.id, batch_number=f"BATCH-{random.randint(10000, 99999)}",
                                quantity_available=random.randint(10, 500), expiry_date=fake.future_date())
        
        db.add(batch)
    
    db.commit()

    print(f"{count} fake inventory batches inserted successfully!")

    db.close()

if __name__ == "__main__":

    # seed_fake_product()
    # seed_inventory_batches()








        


