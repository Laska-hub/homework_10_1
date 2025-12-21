import pytest
from typing import Any

from src.masks import mask_account_number, mask_card_number
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890", "1234 56** 7890"),
        ("123456789012", "1234 56** **12"),
    ],
)
def test_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    ["", "12345", "abcd123456", "1234 5678"],
)
def test_mask_card_number_invalid(card_number: str) -> None:
    with pytest.raises(ValueError):
        mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
        ("00001234", "**1234"),
    ],
)
def test_mask_account_number_valid(account_number: str, expected: str) -> None:
    assert mask_account_number(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    ["", "123", "abcd", "12a4"],
)
def test_mask_account_number_invalid(account_number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_number(account_number)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361 Счет 73654108430135874305", "Visa Platinum 7000 79** **** 6361 Счет **4305"),
    ],
)
def test_mask_account_card(text: str, expected: str) -> None:
    assert mask_account_card(text) == expected
