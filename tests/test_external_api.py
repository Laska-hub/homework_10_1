from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_rub() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 100.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 180.0}

    transaction = {
        "operationAmount": {
            "amount": "2",
            "currency": {"code": "USD"},
        }
    }

    result = convert_to_rub(transaction)
    assert result == 180.0
