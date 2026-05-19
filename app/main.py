from app.models.reservation import Reservation

sample_reservation = Reservation(
    batch_id=1,
    reserved_quantity=5,
    status="RESERVED"
)

print(sample_reservation.batch_id)
print(sample_reservation.reserved_quantity)
print(sample_reservation.status)
print(sample_reservation.reserved_at)


