from src.transactions import process_bank_operations, process_bank_search


def test_process_bank_search() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Оплата счета"},
    ]
    result = process_bank_search(data, "Перевод")
    assert result == [{"description": "Перевод организации"}]

    # Тест на регистр
    result = process_bank_search(data, "перевод")
    assert result == [{"description": "Перевод организации"}]


def test_process_bank_operations() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Оплата счета"},
        {"description": "Перевод зарплаты"},
    ]
    categories = ["Перевод", "Оплата", "Снятие"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 2, "Оплата": 1, "Снятие": 0}
