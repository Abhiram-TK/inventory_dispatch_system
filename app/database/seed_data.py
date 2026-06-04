from faker import Faker

from app.database.connection import SessionLocal

from app.operations.inventory_ops import reserve_inventory

from app.models.product import Product
from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch
from app.models.reservation import Reservation

import random

PRODUCT_CATALOG = { "Laptop": [("Dell Latitude 5440", 72000), ("HP ProBook 450 G9", 68000), ("Lenovo ThinkPad E14", 75000)],

                    "Monitor": [("LG 24MP400", 9500), ("Samsung Essential S3", 12000), ("Dell P2422H", 18500)],

                    "Mouse": [("Logitech M90", 450), ("Logitech M331", 1200), ("Logitech MX Master 3", 8500)],

                    "Keyboard": [("Logitech K120", 650), ("Logitech MK270", 1800), ("Keychron K2", 7800)],

                    "Printer": [("HP LaserJet MFP 136w", 15500), ("Epson EcoTank L3211", 14500), ("Canon PIXMA G3010", 16500)],

                    "Router": [("TP-Link Archer C6", 2600), ("TP-Link Archer AX23", 6200), ("Asus RT-AX58U", 14500)]}

fake = Faker()

def seed_fake_products():

    db = SessionLocal()

    for category in PRODUCT_CATALOG:

        for product_name, price in PRODUCT_CATALOG[category]:

            sku = (category[:3].upper() + "-" + product_name.upper().replace(" ", "").replace("-", ""))

            existing_product = (db.query(Product).filter(Product.sku == sku).first())

            if existing_product:
                continue

            product = Product(name=product_name, sku=sku, price=price)

            db.add(product)

    db.commit()

    print("Realistic product catalog inserted.")

    db.close()

def seed_inventory_batches(count=1000):

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

    seed_fake_products()
    seed_inventory_batches()
    seed_fake_reservations()








        


