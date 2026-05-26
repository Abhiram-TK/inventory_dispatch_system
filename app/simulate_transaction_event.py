from app.events.reservation_event_handler import process_transaction_created

print("\n------ SIMULATING TRANSACTION EVENT ------")

payload = {"transaction_id": 1, "invoice_number": "INV-5001", "product_id": 9999999, "quantity": 2}

process_transaction_created(payload)

print("\n------ EVENT SIMULATION COMPLETED ------")

