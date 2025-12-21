from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по ключу 'state'.
    """
    return [tx for tx in transactions if tx.get("state") == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.
    """
    return sorted(transactions, key=lambda tx: tx["date"], reverse=descending)
