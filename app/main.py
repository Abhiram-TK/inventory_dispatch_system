from app.models.dispatch import Dispatch

sample_dispatch = Dispatch(
    reservation_id=1,
    vehicle_number="KA01AB1234",
    status="IN_TRANSIT"
)

print(sample_dispatch.reservation_id)
print(sample_dispatch.vehicle_number)
print(sample_dispatch.status)
print(sample_dispatch.dispatch_date)