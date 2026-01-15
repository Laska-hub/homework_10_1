import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected
