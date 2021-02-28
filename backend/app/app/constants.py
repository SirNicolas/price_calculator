from enum import Enum
from decimal import Decimal


class PriceDiscount:
    discounts = {1000: 3, 5000: 5, 7000: 7, 10000: 10, 50000: 15}

    @classmethod
    def get_discount(cls, price: Decimal) -> int:
        total_discount = 0

        for total_price, discount in cls.discounts.items():
            if price >= total_price:
                total_discount = discount
            else:
                break

        return total_discount


class StateEnum(str, Enum):
    UT = "UT"
    NV = "NV"
    TX = "TX"
    AL = "AL"
    CA = "CA"


class StateTaxEnum(Enum):
    UT = Decimal(6.85)
    NV = Decimal(8)
    TX = Decimal(6.25)
    AL = Decimal(4)
    CA = Decimal(8.25)
