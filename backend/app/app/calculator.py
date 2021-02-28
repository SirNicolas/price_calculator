from typing import Tuple
from decimal import Decimal

from app.constants import PriceDiscount, StateTaxEnum
from app.schemas.calculation import Calculation


class Calculator:

    def __init__(self, quantity: int, price_per_item: Decimal, state: str):
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.state = state

    def _calculate_discount(self) -> Tuple[Decimal, int]:
        raw_total_price = self.quantity * self.price_per_item
        discount = PriceDiscount.get_discount(raw_total_price)
        price_with_discount = raw_total_price * (100 - discount) / 100
        return price_with_discount, discount

    def _calculate_tax(self, price_with_discount: Decimal) -> Tuple[Decimal, Decimal]:
        state_tax = StateTaxEnum[self.state.upper()].value
        return price_with_discount * state_tax / 100, state_tax

    def execute(self):
        price_with_discount, discount = self._calculate_discount()
        tax, state_tax = self._calculate_tax(price_with_discount)
        final_price = price_with_discount + tax
        return Calculation(
            quantity=self.quantity,
            price_per_item=self.price_per_item,
            state=self.state,
            final_price=final_price,
            price_with_discount=price_with_discount,
            discount=discount,
            tax=tax,
            state_tax=state_tax,
        )
