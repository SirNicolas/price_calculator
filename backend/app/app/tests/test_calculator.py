import pytest
from decimal import Decimal

from app.calculator import Calculator
from app.schemas.calculation import Calculation
from app.tests.constants import CALCULATOR_PARAMS, CALCULATOR_FIELDS


@pytest.mark.parametrize(
    CALCULATOR_FIELDS,
    CALCULATOR_PARAMS,
)
def test_calculator(
        quantity, price_per_item, state, discount, price_with_discount, tax, state_tax, final_price
) -> None:
    price_per_item = Decimal(price_per_item)
    expected_calculation = Calculation(
        quantity=quantity,
        price_per_item=price_per_item,
        state=state,
        discount=discount,
        price_with_discount=price_with_discount,
        tax=tax,
        state_tax=state_tax,
        final_price=final_price,
    )
    calculation = Calculator(quantity=quantity, price_per_item=price_per_item, state=state).execute()
    assert expected_calculation == calculation
