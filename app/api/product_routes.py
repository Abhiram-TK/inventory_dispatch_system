from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductResponse

router = APIRouter(tags=["Products"])

@router.get("/products", response_model=list[ProductResponse], summary="View Products", description="""
            Retrieve all available products.

            Returns product master data including:

            - Product ID
            - Product Name
            - SKU
            - Price

            Used as the starting point for inventory lookup and reservation workflows.
            """)

def get_products(db: Session = Depends(get_db)):

    return db.query(Product).all()