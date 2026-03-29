# backend/routes/vin_routes.py
from fastapi import APIRouter

router = APIRouter(prefix="/vin", tags=["VIN"])

@router.get("/{vin}")
async def vin_lookup(vin: str):
    # Demo response for testing
    return {
        "vin": vin,
        "make": "Honda",
        "model": "Accord",
        "year": "2003",
        "trim": "EX"
    }
