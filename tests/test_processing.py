import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


def test_filter_by_state_default(sample_transactions):
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(tx["state"] == "EXECUTED" for tx in result)


def test_filter_by_state_custom(sample_transactions):
    result = filter_by_state(sample_transactions, state="CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_sort_by_date_descending(sample_transactions):
    result = sort_by_date(sample_transactions)
    dates = [tx["date"] for tx in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, descending=False)
    dates = [tx["date"] for tx in result]
    assert dates == sorted(dates)
