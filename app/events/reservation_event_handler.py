# Handles inventory reservation events

from app.database.connection import SessionLocal

from app.models.inventory_batch import InventoryBatch
from app.models.dispatch import Dispatch
from app.models.reservation import Reservation
from app.models.product import Product

from app.operations.inventory_ops import reserve_inventory

def write_log(message):

    with open("app/inventory_events.log", "a") as log_file:

        log_file.write(message + "\n")

def process_transaction_created(payload):

    print("\nTRANSACTION_CREATED event received")

    write_log("\nTRANSACTION_CREATED event received")

    print(f"\nPayload: {payload}")

    write_log(f"Payload: {payload}")

    transaction_id = payload["transaction_id"]

    invoice_number = payload["invoice_number"]

    product_id = payload["product_id"]

    quantity = payload["quantity"]

    db = SessionLocal()

    batch = db.query(InventoryBatch).filter(InventoryBatch.product_id == product_id).first()

    if not batch:

        print("No inventory batch found.")

        write_log(f"Reservation failed | Invalid product_id: {product_id}")

        db.close()

        return
    
    print("\nProcessing reservation......")

    print(f"\nAttempting reservation for Product ID: {product_id}")

    print(f"Requested Quantity: {quantity}")

    try:

        reservation = reserve_inventory(batch_id=batch.id, reserve_quantity=quantity)

        print("\nInventory reserved successfully!")

        write_log(f"Reservation successful | Product ID: {product_id} | Quantity: {quantity}")

        print(f"\nReservation ID: {reservation.id}")

        print(f"Reserved Quantity: {reservation.reserved_quantity}")

    except Exception as e:

        print("\nInventory reservation failed.")

        write_log(f"Reservation failed: {str(e)}")

        print(f"\nReason: {str(e)}")
        
        print("\nPossible causes:")

        print("- insufficient inventory")

        print("- invalid inventory batch")

        print("- reservation rollback triggered")

    print("\nEvent processing completed.")

    db.close()

