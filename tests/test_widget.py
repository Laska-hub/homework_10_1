import pytest
from widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        (
            "Счет 73654108430135874305",
            "Счет **4305",
        ),
    ],
)
def test_mask_account_card_valid(data, expected):
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "data",
    [
        "",
        "Visa",
        "Счет",
        "Visa Platinum ABCD",
    ],
)
def test_mask_account_card_invalid(data):
    with pytest.raises(Exception):
        mask_account_card(data)


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-01-01T00:00:00", "01.01.2019"),
    ],
)
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected


@pytest.mark.parametrize(
    "date_str",
    [
        "",
        "2024-13-01",
        "not-a-date",
    ],
)
def test_get_date_invalid(date_str):
    with pytest.raises(ValueError):
        get_date(date_str)