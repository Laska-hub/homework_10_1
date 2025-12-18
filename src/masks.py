"""Реализуйте в этом модуле две функции:
Функцию маскировки номера банковской карты get_mask_card_number.
Функцию маскировки номера банковского счета get_mask_account.
"""

from typing import List


def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маску номера карты в формате XXXX XX** **** XXXX.
    Видны первые 6 и последние 4 цифры, остальные скрыты.
    """
    if not card_number.isdigit() or len(card_number) < 10:
        raise ValueError("Номер карты должен содержать только цифры " "и иметь длину не менее 10 символов")

    first_six = card_number[:6]
    last_four = card_number[-4:]
    hidden_part = card_number[6:-4]
    masked_middle = "*" * len(hidden_part)
    masked_number = f"{first_six}{masked_middle}{last_four}"

    blocks: List[str] = [masked_number[i : i + 4] for i in range(0, len(masked_number), 4)]
    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску банковского счёта в формате **XXXX.
    Видны только последние 4 цифры.
    """
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Номер счета должен содержать хотя бы 4 цифры")

    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
