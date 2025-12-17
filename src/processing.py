from typing import Dict, List


def filter_by_state(
    transactions: List[Dict],
    state: str = "EXECUTED",
) -> List[Dict]:
    """
    Фильтрует список словарей с банковскими операциями
    по ключу 'state'.

    Args:
        transactions (List[Dict]):
            Список словарей с операциями.
        state (str, optional):
            Значение ключа 'state' для фильтрации.
            По умолчанию "EXECUTED".

    Returns:
        List[Dict]:
            Новый список словарей с указанным состоянием.
    """
    return [
        transaction
        for transaction in transactions
        if transaction.get("state") == state
    ]


def sort_by_date(
    transactions: List[Dict],
    descending: bool = True,
) -> List[Dict]:
    """
    Сортирует список словарей с операциями по дате.

    Args:
        transactions (List[Dict]):
            Список словарей с операциями.
        descending (bool, optional):
            True — по убыванию,
            False — по возрастанию.
            По умолчанию True.

    Returns:
        List[Dict]:
            Новый список словарей, отсортированный по дате.
    """
    return sorted(
        transactions,
        key=lambda transaction: transaction["date"],
        reverse=descending,
    )


if __name__ == "__main__":
    data = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]

    print("Фильтрация по умолчанию ('EXECUTED'):")
    print(filter_by_state(data))

    print("\nФильтрация по 'CANCELED':")
    print(filter_by_state(data, state="CANCELED"))

    print("\nСортировка по дате (по убыванию):")
    print(sort_by_date(data))

    print("\nСортировка по дате (по возрастанию):")
    print(sort_by_date(data, descending=False))
