import re
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, где в описании есть строка `search`.
    Использует регулярные выражения.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.
    """
    descriptions = [item.get("description", "") for item in data]
    counts: Dict[str, int] = {}
    for category in categories:
        counts[category] = sum(1 for desc in descriptions if category.lower() in desc.lower())
    return counts


if __name__ == "__main__":
    # Пример данных
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата счета"},
        {"description": "Перевод организации"},
    ]

    search_result = process_bank_search(data, "перевод")
    print("Результаты поиска по 'перевод':")
    print(search_result)

    categories = ["перевод", "оплата"]
    category_counts = process_bank_operations(data, categories)
    print("Количество операций по категориям:")
    print(category_counts)
