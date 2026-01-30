"""Работа с внешним API для конвертации валют."""

from __future__ import annotations

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY: str | None = os.getenv("EXCHANGE_API_KEY")
URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Если валюта RUB — возвращает сумму.
    Если другая валюта — делает запрос к API и возвращает result.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    headers = {"apikey": API_KEY}
    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(URL, headers=headers, params=params, timeout=10)
    data: Dict[str, Any] = response.json()

    if "result" not in data:
        raise ValueError(f"Не удалось получить результат конвертации: {data}")

    return float(data["result"])


if __name__ == "__main__":
    example_transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"},
        }
    }
    rub_amount = convert_to_rub(example_transaction)
    print(f"Сумма в рублях: {rub_amount:.2f}")
