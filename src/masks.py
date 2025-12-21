"""Реализуйте в этом модуле две функции:
Функцию маскировки номера банковской карты mask_card_number.
Функцию маскировки номера банковского счета mask_account_number.
"""

import re


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""
    if not card_number.isdigit() or len(card_number) not in [10, 12, 16]:
        raise ValueError("Неверный формат номера карты")

    if len(card_number) == 10:
        return f"{card_number[:4]} {card_number[4:6]}** {card_number[-4:]}"
    if len(card_number) == 12:
        return f"{card_number[:4]} {card_number[4:6]}** **{card_number[-2:]}"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры видимыми"""
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Неверный формат номера счета")
    return f"**{account_number[-4:]}"


def mask_account_card(text: str) -> str:
    """Ищет и маскирует все номера карт и счетов в тексте"""
    text = re.sub(
        r"(\d{10}|\d{12}|\d{16})",
        lambda m: mask_card_number(m.group()),
        text,
    )
    text = re.sub(r"\d{4,20}", lambda m: mask_account_number(m.group()), text)
    return text
