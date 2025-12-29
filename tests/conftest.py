import pytest


@pytest.fixture
def transactions() -> list[dict[str, str]]:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "2", "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "3", "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": "4", "state": "PENDING", "date": "2019-01-01T10:00:00.000000"},
    ]
