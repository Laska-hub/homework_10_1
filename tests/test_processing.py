import pytest
from processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(transactions, state, expected_ids):
    result = filter_by_state(transactions, state)
    assert [tx["id"] for tx in result] == expected_ids


def test_filter_by_state_default(transactions):
    result = filter_by_state(transactions)
    assert all(tx["state"] == "EXECUTED" for tx in result)


def test_filter_by_state_empty():
    assert filter_by_state([]) == []


def test_sort_by_date_desc(transactions):
    result = sort_by_date(transactions)
    dates = [tx["date"] for tx in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(transactions):
    result = sort_by_date(transactions, descending=False)
    dates = [tx["date"] for tx in result]
    assert dates == sorted(dates)


def test_sort_by_date_same_dates():
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
    ]
    result = sort_by_date(data)
    assert len(result) == 2


def test_sort_by_date_missing_date_key():
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])