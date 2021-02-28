from typing import Any

from fastapi import APIRouter

from app.schemas import calculation as schemas
from app.calculator import Calculator

router = APIRouter()


@router.post("/", response_model=schemas.Calculation)
def calculate(
    calculation_data: schemas.CalculationCreate,
) -> Any:
    """
    Calculate price with discount and state taxes
    """
    return Calculator(
        quantity=calculation_data.quantity,
        price_per_item=calculation_data.price_per_item,
        state=calculation_data.state
    ).execute()
