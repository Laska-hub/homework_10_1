from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

Transaction = Dict[str, Any]


@pytest.fixture
def transactions() -> List[Transaction]:
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
        },
        {
            "id": 4,
            "description": "Некорректная транзакция",
        },
    ]


# filter_by_currency


def test_filter_by_currency_usd(
    transactions: List[Transaction],
) -> None:
    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in result)


def test_filter_by_currency_no_matches(
    transactions: List[Transaction],
) -> None:
    result = list(filter_by_currency(transactions, "GBP"))

    assert result == []


# transaction_descriptions


def test_transaction_descriptions(
    transactions: List[Transaction],
) -> None:
    descriptions = list(transaction_descriptions(transactions))

    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Некорректная транзакция",
    ]


# card_number_generator


def test_card_number_generator_valid_range() -> None:
    result = list(card_number_generator(1, 3))

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


@pytest.mark.parametrize(
    ("start", "end"),
    [
        (0, 5),
        (5, 4),
        (1, 10_000_000_000_000_000),
    ],
)
def test_card_number_generator_invalid_range(
    start: int,
    end: int,
) -> None:
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))
