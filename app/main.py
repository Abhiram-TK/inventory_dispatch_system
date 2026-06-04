from fastapi import FastAPI

import app.models

from app.api.inventory_routes import router as inventory_router
from app.api.dispatch_routes import router as dispatch_router

from app.core.logger import logger

app = FastAPI(title="Inventory Reservation & Dispatch System", version="1.0.0")

logger.info("Inventory API started")

app.include_router(inventory_router)

app.include_router(dispatch_router)


@app.get("/")
def home():

    return {
        "message": "Inventory Reservation & Dispatch System Running"
    }