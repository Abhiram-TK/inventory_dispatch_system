from celery import Celery

celery_app = Celery("inventory_worker", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

celery_app.conf.beat_schedule = {"expire-reservations-every-minute": {"task": "app.workers.reservation_tasks.expire_reservation", "schedule": 60.0}}

celery_app.conf.timezone = "UTC"

import app.workers.reservation_tasks