"""Реализуйте в этом модуле две функции:
Функцию маскировки номера банковской карты mask_card_number.
Функцию маскировки номера банковского счета mask_account_number.
"""
def mask_card_number(card_number: str) -> str:
    if not card_number.isdigit() or len(card_number) < 10:
        raise ValueError("Invalid card number")

    first4 = card_number[:4]
    next2 = card_number[4:6]

    length = len(card_number)

    if length == 10:
        return f"{first4} {next2}** {card_number[-4:]}"

    if length == 12:
        return f"{first4} {next2}** **{card_number[-2:]}"

    stars = "*" * (length - 10)
    middle = f"{stars[:2]} {stars[2:]}" if len(stars) > 2 else stars

    return f"{first4} {next2}{middle} {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Invalid account number")

    return f"**{account_number[-4:]}"


def mask_account_card(text: str) -> str:
    parts = text.split()
    result = []

    i = 0
    while i < len(parts):
        if parts[i] == "Счет" and i + 1 < len(parts):
            result.append("Счет")
            result.append(mask_account_number(parts[i + 1]))
            i += 2
        elif parts[i].isdigit():
            result.append(mask_card_number(parts[i]))
            i += 1
        else:
            result.append(parts[i])
            i += 1

    return " ".join(result)
