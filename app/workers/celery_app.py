from celery import Celery

celery_app = Celery("inventory_worker", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

import app.workers.reservation_tasks