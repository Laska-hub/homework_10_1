# tests/test_external_api.py

from typing import Any, Dict
from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_rub() -> None:
    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 100.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get) -> None:
    # Мокаем ответ API
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}

    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "2",
            "currency": {"code": "USD"},
        }
    }

    result = convert_to_rub(transaction)
    assert result == 180.0  # 2 * 90
