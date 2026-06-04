from fastapi import APIRouter

router = APIRouter()

@router.get("/inventory")

def get_inventory():

    return {"message": "Inventory endpoint working"}