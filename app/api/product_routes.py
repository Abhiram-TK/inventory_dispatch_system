from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductResponse

router = APIRouter()

@router.get("/products", response_model=list[ProductResponse])

def get_products(db: Session = Depends(get_db)):

    return db.query(Product).all()