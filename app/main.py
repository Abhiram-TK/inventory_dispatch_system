from fastapi import FastAPI

import app.models

from app.api.event_routes import router as evennt_router
from app.api.product_routes import router as product_router
from app.api.inventory_routes import router as inventory_router
from app.api.reservation_routes import router as reservation_router
from app.api.dispatch_routes import router as dispatch_router

from app.core.logger import logger

app = FastAPI(title="Inventory Reservation & Dispatch System", version="1.0.0")

logger.info("Inventory API started")

app.include_router(evennt_router, tags=["Events"])
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(reservation_router)
app.include_router(dispatch_router)

@app.get("/", tags=["System"], summary="Health Check", description="""
        Check service health.

        Returns current application status.""")

def home():

    return {"message": "Inventory Reservation & Dispatch System Running"}