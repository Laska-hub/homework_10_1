import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")  # ключ из .env
URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта RUB — возвращает сумму как float.
    Если валюта USD или EUR — делает запрос к API и конвертирует.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    # Заголовки и параметры запроса
    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    response = requests.get(URL, headers=headers, params=params)

    try:
        data = response.json()
    except ValueError:
        raise ValueError("Ошибка при чтении JSON из ответа API")

    # Проверяем, есть ли rates
    if "rates" not in data or "RUB" not in data["rates"]:
        raise ValueError(f"Не удалось получить курс валют: {data}")

    rate = data["rates"]["RUB"]
    return amount * rate


# Пример использования
if __name__ == "__main__":
    transaction_example = {
        "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}
    }
    rub_amount = convert_to_rub(transaction_example)
    print(f"Сумма в рублях: {rub_amount:.2f}")
