"""
Функции форматирования строк выводимых в виджете.
Здесь происходит использование функций из masks, без дублирования логики.
"""

from datetime import datetime

from masks import mask_account_number, mask_card_number


def mask_account_card(data: str) -> str:
    """
    Принимает строку:
    'Visa Platinum 7000792289606361'
    'Счет 73654108430135874305'

    Определяет тип — карта или счет:
    - если начинается со слова "Счет" → счёт
    - иначе → карта

    Возвращает замаскированный номер, используя функции из masks.
    """
    name, number = data.rsplit(" ", 1)

    if name.lower().startswith("счет"):
        masked = mask_account_number(number)
    else:
        masked = mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """
    Принимает дату вида:
    '2024-03-11T02:26:18.671407'

    Возвращает дату в формате '11.03.2024'.
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))