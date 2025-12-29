from typing import Any, Dict, Iterator, List

Transaction = Dict[str, Any]


def filter_by_currency(
    transactions: List[Transaction],
    currency_code: str,
) -> Iterator[Transaction]:
    """
    Генератор транзакций, отфильтрованных по коду валюты.

    :param transactions: список транзакций
    :param currency_code: код валюты (например, 'USD')
    :return: итератор транзакций
    """
    for transaction in transactions:
        try:
            currency = transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            continue

        if currency == currency_code:
            yield transaction


def transaction_descriptions(
    transactions: List[Transaction],
) -> Iterator[str]:
    """
    Генератор описаний транзакций.

    :param transactions: список транзакций
    :return: итератор описаний операций
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (включительно)
    :param end: конечное значение (включительно)
    :return: итератор номеров карт
    """
    if start < 1 or end > 9999_9999_9999_9999 or start > end:
        raise ValueError("Некорректный диапазон номеров карт")

    for number in range(start, end + 1):
        digits = f"{number:016d}"
        yield (f"{digits[0:4]} " f"{digits[4:8]} " f"{digits[8:12]} " f"{digits[12:16]}")
