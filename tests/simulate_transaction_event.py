from app.events.reservation_event_handler import process_transaction_created

print("\n------ SIMULATING TRANSACTION EVENT ------")

payload = {"transaction_id": 1001, "invoice_number": "INV-1001", "product_id": 1, "quantity": 5}

process_transaction_created(payload)

print("\n------ EVENT SIMULATION COMPLETED ------")