from fastapi import APIRouter

router = APIRouter()

@router.get("/dispatch")

def get_dispatch():

    return {"message": "Dispatch endpoint working"}