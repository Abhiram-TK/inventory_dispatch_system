from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductResponse

from app.services.permission_checker import PermissionChecker

router = APIRouter(tags=["Products"])

@router.get("/products", response_model=list[ProductResponse], summary="View Products", dependencies=[Depends(PermissionChecker(["view_products"]))], description="""
            Retrieve available products.

            Requires:

            - view_products permission

            Returns available products with pricing information.""")

def get_products(db: Session = Depends(get_db)):

    return db.query(Product).all()