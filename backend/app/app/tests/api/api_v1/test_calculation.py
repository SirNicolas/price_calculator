import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.tests.constants import CALCULATOR_PARAMS, CALCULATOR_FIELDS


@pytest.mark.parametrize(
    CALCULATOR_FIELDS,
    CALCULATOR_PARAMS,
)
def test_create_calculation(
        client: TestClient, quantity, price_per_item, state, discount, price_with_discount, tax, state_tax, final_price
) -> None:
    data = {"quantity": quantity, "price_per_item": price_per_item, "state": state}
    response = client.post(
        f"{settings.API_V1_STR}/calculation/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["quantity"] == quantity
    assert content["price_per_item"] == price_per_item
    assert content["state"] == state
    assert content["discount"] == discount
    assert content["price_with_discount"] == price_with_discount
    assert content["tax"] == tax
    assert content["state_tax"] == state_tax
    assert content["final_price"] == final_price


@pytest.mark.parametrize(
    ["quantity", "price_per_item", "state", "error_message"],
    [
        (0, 1000, "AL", {
            'detail': [{
                'loc': ['body', 'calculation_data', 'quantity'],
                'msg': 'ensure this value is greater than 0',
                'type': 'value_error.number.not_gt', 'ctx': {'limit_value': 0}
            }]
        }),
        (-1, 1000, "AL", {
            'detail': [{
                'loc': ['body', 'calculation_data', 'quantity'],
                'msg': 'ensure this value is greater than 0',
                'type': 'value_error.number.not_gt', 'ctx': {'limit_value': 0}
            }]
        }),
        (1, 0, "AL", {
            'detail': [{
                'loc': ['body', 'calculation_data', 'price_per_item'],
                'msg': 'ensure this value is greater than 0',
                'type': 'value_error.number.not_gt', 'ctx': {'limit_value': 0}
            }]
        }),
        (1, 1000, "MO", {
            'detail': [{
                'ctx': {'enum_values': ['UT', 'NV', 'TX', 'AL', 'CA']},
                'loc': ['body', 'calculation_data', 'state'],
                'msg': "value is not a valid enumeration member; permitted: 'UT', 'NV', 'TX', 'AL', 'CA'",
                'type': 'type_error.enum'
            }]
        }),
    ],
    ids=[
        "Quantity is 0",
        "Quantity is negative",
        "Price is 0",
        "State is incorrect",
    ]
)
def test_create_calculation_failed(client: TestClient, quantity, price_per_item, state, error_message) -> None:
    data = {"quantity": quantity, "price_per_item": price_per_item, "state": state}
    response = client.post(
        f"{settings.API_V1_STR}/calculation/", json=data,
    )
    assert response.status_code == 422
    content = response.json()
    assert content == error_message
