"""
Функции форматирования строк выводимых в виджете.
Здесь происходит использование функций из masks, без дублирования логики.
"""

from datetime import datetime

from .masks import mask_account_card


def get_date(iso_string: str) -> str:
    """Преобразует ISO дату в dd.mm.yyyy"""
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%d.%m.%Y")


def mask_account_card_widget(text: str) -> str:
    """Просто проксирует вызов из masks.py для виджета"""
    return mask_account_card(text)
