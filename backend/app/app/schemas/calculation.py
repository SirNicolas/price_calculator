from decimal import Decimal
from pydantic import BaseModel, condecimal, conint

from app.constants import StateEnum


class CalculationCreate(BaseModel):
    quantity: conint(gt=0)
    price_per_item: condecimal(gt=0)
    state: StateEnum


class Calculation(CalculationCreate):
    discount: int
    price_with_discount: Decimal
    tax: Decimal
    final_price: Decimal
    state_tax: Decimal
