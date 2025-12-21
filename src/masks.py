"""Реализуйте в этом модуле две функции:
Функцию маскировки номера банковской карты mask_card_number.
Функцию маскировки номера банковского счета mask_account_number.
"""
"""Модуль для маскировки номеров карт и счетов"""

import re

def mask_card_number(card_number: str) -> str:
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit() or len(card_number) not in (10, 12, 16):
        raise ValueError("Invalid card number")

    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 12:
        return f"{card_number[:4]} {card_number[4:6]}** **{card_number[-2:]}"
    else:  # 10
        return f"{card_number[:4]} {card_number[4:6]}** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    account_number = account_number.replace(" ", "")
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Invalid account number")
    return f"**{account_number[-4:]}"


def mask_account_card(text: str) -> str:
    words = text.split()
    masked_words = []
    for word in words:
        clean_word = re.sub(r'\D', '', word)  # оставляем только цифры для проверки
        if clean_word.isdigit():
            if 10 <= len(clean_word) <= 16:
                masked_words.append(mask_card_number(clean_word))
            elif len(clean_word) >= 4:
                masked_words.append(mask_account_number(clean_word))
            else:
                masked_words.append(word)
        else:
            masked_words.append(word)
    return ' '.join(masked_words)
